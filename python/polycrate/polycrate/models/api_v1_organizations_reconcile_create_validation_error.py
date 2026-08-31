from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_reconcile_create_active_error_component import (
        ApiV1OrganizationsReconcileCreateActiveErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_actual_availability_error_component import (
        ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_alias_error_component import (
        ApiV1OrganizationsReconcileCreateAliasErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_annotations_error_component import (
        ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_archived_at_error_component import (
        ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_archived_by_error_component import (
        ApiV1OrganizationsReconcileCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_archived_error_component import (
        ApiV1OrganizationsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_archived_reason_error_component import (
        ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_endpoint_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_lb_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_logs_30d_error_component import (
        ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_member_active_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_member_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_s3_object_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_total_product_cost_error_component import (
        ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_volume_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_cached_workspace_count_error_component import (
        ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_color_error_component import (
        ApiV1OrganizationsReconcileCreateColorErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_created_by_component_error_component import (
        ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_created_by_user_error_component import (
        ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_criticality_error_component import (
        ApiV1OrganizationsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_debug_mode_error_component import (
        ApiV1OrganizationsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_description_error_component import (
        ApiV1OrganizationsReconcileCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_discovery_enabled_error_component import (
        ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_display_name_error_component import (
        ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_domains_error_component import (
        ApiV1OrganizationsReconcileCreateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_emails_error_component import (
        ApiV1OrganizationsReconcileCreateEmailsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_endpoint_monitors_error_component import (
        ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_gitlab_group_id_error_component import (
        ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_gitlab_group_url_error_component import (
        ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_grafana_org_id_error_component import (
        ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_group_id_error_component import (
        ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_project_id_error_component import (
        ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_icon_content_type_error_component import (
        ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_icon_filename_error_component import (
        ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_kind_error_component import (
        ApiV1OrganizationsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_labels_error_component import (
        ApiV1OrganizationsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_legal_name_error_component import (
        ApiV1OrganizationsReconcileCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_loopback_org_id_error_component import (
        ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_loopback_project_id_error_component import (
        ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_managed_by_content_type_error_component import (
        ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_managed_by_object_id_error_component import (
        ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_modified_by_user_error_component import (
        ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_name_error_component import (
        ApiV1OrganizationsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_non_field_errors_error_component import (
        ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_observability_metrics_error_component import (
        ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_owner_id_error_component import (
        ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_platform_dns_record_created_error_component import (
        ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_platform_service_error_component import (
        ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_priority_error_component import (
        ApiV1OrganizationsReconcileCreatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_provider_error_component import (
        ApiV1OrganizationsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_provider_id_error_component import (
        ApiV1OrganizationsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_provider_reference_error_component import (
        ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_scope_error_component import (
        ApiV1OrganizationsReconcileCreateScopeErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_sla_availability_error_component import (
        ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_sla_target_error_component import (
        ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_sla_window_days_error_component import (
        ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_slo_availability_error_component import (
        ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_slo_target_error_component import (
        ApiV1OrganizationsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_slo_window_days_error_component import (
        ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_slug_error_component import (
        ApiV1OrganizationsReconcileCreateSlugErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_target_availability_error_component import (
        ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_unified_harbor_credential_error_component import (
        ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_upstream_organization_id_error_component import (
        ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_upstream_system_id_error_component import (
        ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_urls_error_component import (
        ApiV1OrganizationsReconcileCreateUrlsErrorComponent,
    )
    from ..models.api_v1_organizations_reconcile_create_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsReconcileCreateValidationError")


@_attrs_define
class ApiV1OrganizationsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsReconcileCreateActiveErrorComponent |
            ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent |
            ApiV1OrganizationsReconcileCreateAliasErrorComponent |
            ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent |
            ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent |
            ApiV1OrganizationsReconcileCreateArchivedByErrorComponent |
            ApiV1OrganizationsReconcileCreateArchivedErrorComponent |
            ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent |
            ApiV1OrganizationsReconcileCreateColorErrorComponent |
            ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent |
            ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent |
            ApiV1OrganizationsReconcileCreateCriticalityErrorComponent |
            ApiV1OrganizationsReconcileCreateDebugModeErrorComponent |
            ApiV1OrganizationsReconcileCreateDescriptionErrorComponent |
            ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent |
            ApiV1OrganizationsReconcileCreateDomainsErrorComponent | ApiV1OrganizationsReconcileCreateEmailsErrorComponent |
            ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent |
            ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent |
            ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent |
            ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent |
            ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent |
            ApiV1OrganizationsReconcileCreateKindErrorComponent | ApiV1OrganizationsReconcileCreateLabelsErrorComponent |
            ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsReconcileCreateLegalNameErrorComponent |
            ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent |
            ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent |
            ApiV1OrganizationsReconcileCreateNameErrorComponent |
            ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent |
            ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent |
            ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent |
            ApiV1OrganizationsReconcileCreatePriorityErrorComponent |
            ApiV1OrganizationsReconcileCreateProviderErrorComponent |
            ApiV1OrganizationsReconcileCreateProviderIdErrorComponent |
            ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent |
            ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent |
            ApiV1OrganizationsReconcileCreateScopeErrorComponent |
            ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent |
            ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent |
            ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1OrganizationsReconcileCreateSloTargetErrorComponent |
            ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent |
            ApiV1OrganizationsReconcileCreateSlugErrorComponent |
            ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent |
            ApiV1OrganizationsReconcileCreateUrlsErrorComponent |
            ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsReconcileCreateActiveErrorComponent
        | ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent
        | ApiV1OrganizationsReconcileCreateAliasErrorComponent
        | ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent
        | ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent
        | ApiV1OrganizationsReconcileCreateArchivedByErrorComponent
        | ApiV1OrganizationsReconcileCreateArchivedErrorComponent
        | ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsReconcileCreateColorErrorComponent
        | ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent
        | ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent
        | ApiV1OrganizationsReconcileCreateCriticalityErrorComponent
        | ApiV1OrganizationsReconcileCreateDebugModeErrorComponent
        | ApiV1OrganizationsReconcileCreateDescriptionErrorComponent
        | ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent
        | ApiV1OrganizationsReconcileCreateDomainsErrorComponent
        | ApiV1OrganizationsReconcileCreateEmailsErrorComponent
        | ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent
        | ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent
        | ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsReconcileCreateKindErrorComponent
        | ApiV1OrganizationsReconcileCreateLabelsErrorComponent
        | ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsReconcileCreateLegalNameErrorComponent
        | ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent
        | ApiV1OrganizationsReconcileCreateNameErrorComponent
        | ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent
        | ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent
        | ApiV1OrganizationsReconcileCreatePriorityErrorComponent
        | ApiV1OrganizationsReconcileCreateProviderErrorComponent
        | ApiV1OrganizationsReconcileCreateProviderIdErrorComponent
        | ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent
        | ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsReconcileCreateScopeErrorComponent
        | ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent
        | ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1OrganizationsReconcileCreateSloTargetErrorComponent
        | ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent
        | ApiV1OrganizationsReconcileCreateSlugErrorComponent
        | ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsReconcileCreateUrlsErrorComponent
        | ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_reconcile_create_active_error_component import (
            ApiV1OrganizationsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_actual_availability_error_component import (
            ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_alias_error_component import (
            ApiV1OrganizationsReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_annotations_error_component import (
            ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_at_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_by_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_reason_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_member_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_volume_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_color_error_component import (
            ApiV1OrganizationsReconcileCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_created_by_component_error_component import (
            ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_created_by_user_error_component import (
            ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_criticality_error_component import (
            ApiV1OrganizationsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_debug_mode_error_component import (
            ApiV1OrganizationsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_description_error_component import (
            ApiV1OrganizationsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_discovery_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_display_name_error_component import (
            ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_domains_error_component import (
            ApiV1OrganizationsReconcileCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_emails_error_component import (
            ApiV1OrganizationsReconcileCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_grafana_org_id_error_component import (
            ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_group_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_project_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_icon_content_type_error_component import (
            ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_icon_filename_error_component import (
            ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_kind_error_component import (
            ApiV1OrganizationsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_labels_error_component import (
            ApiV1OrganizationsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_legal_name_error_component import (
            ApiV1OrganizationsReconcileCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_loopback_org_id_error_component import (
            ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_loopback_project_id_error_component import (
            ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_modified_by_user_error_component import (
            ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_name_error_component import (
            ApiV1OrganizationsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_non_field_errors_error_component import (
            ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_observability_metrics_error_component import (
            ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_owner_id_error_component import (
            ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_platform_service_error_component import (
            ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_priority_error_component import (
            ApiV1OrganizationsReconcileCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_error_component import (
            ApiV1OrganizationsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_id_error_component import (
            ApiV1OrganizationsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_reference_error_component import (
            ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_scope_error_component import (
            ApiV1OrganizationsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_availability_error_component import (
            ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_target_error_component import (
            ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_window_days_error_component import (
            ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_availability_error_component import (
            ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_target_error_component import (
            ApiV1OrganizationsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_window_days_error_component import (
            ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slug_error_component import (
            ApiV1OrganizationsReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_target_availability_error_component import (
            ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_upstream_system_id_error_component import (
            ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_urls_error_component import (
            ApiV1OrganizationsReconcileCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_organizations_reconcile_create_active_error_component import (
            ApiV1OrganizationsReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_actual_availability_error_component import (
            ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_alias_error_component import (
            ApiV1OrganizationsReconcileCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_annotations_error_component import (
            ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_at_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_by_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_archived_reason_error_component import (
            ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_member_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_volume_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_color_error_component import (
            ApiV1OrganizationsReconcileCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_created_by_component_error_component import (
            ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_created_by_user_error_component import (
            ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_criticality_error_component import (
            ApiV1OrganizationsReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_debug_mode_error_component import (
            ApiV1OrganizationsReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_description_error_component import (
            ApiV1OrganizationsReconcileCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_discovery_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_display_name_error_component import (
            ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_domains_error_component import (
            ApiV1OrganizationsReconcileCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_emails_error_component import (
            ApiV1OrganizationsReconcileCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_endpoint_monitors_error_component import (
            ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_grafana_org_id_error_component import (
            ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_group_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_project_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_icon_content_type_error_component import (
            ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_icon_filename_error_component import (
            ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_kind_error_component import (
            ApiV1OrganizationsReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_labels_error_component import (
            ApiV1OrganizationsReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_legal_name_error_component import (
            ApiV1OrganizationsReconcileCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_loopback_org_id_error_component import (
            ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_loopback_project_id_error_component import (
            ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_modified_by_user_error_component import (
            ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_name_error_component import (
            ApiV1OrganizationsReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_non_field_errors_error_component import (
            ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_observability_metrics_error_component import (
            ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_owner_id_error_component import (
            ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_platform_service_error_component import (
            ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_priority_error_component import (
            ApiV1OrganizationsReconcileCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_error_component import (
            ApiV1OrganizationsReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_id_error_component import (
            ApiV1OrganizationsReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_provider_reference_error_component import (
            ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_scope_error_component import (
            ApiV1OrganizationsReconcileCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_availability_error_component import (
            ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_target_error_component import (
            ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_sla_window_days_error_component import (
            ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_availability_error_component import (
            ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_target_error_component import (
            ApiV1OrganizationsReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slo_window_days_error_component import (
            ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_slug_error_component import (
            ApiV1OrganizationsReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_target_availability_error_component import (
            ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_upstream_system_id_error_component import (
            ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_urls_error_component import (
            ApiV1OrganizationsReconcileCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_reconcile_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsReconcileCreateActiveErrorComponent
                | ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent
                | ApiV1OrganizationsReconcileCreateAliasErrorComponent
                | ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent
                | ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent
                | ApiV1OrganizationsReconcileCreateArchivedByErrorComponent
                | ApiV1OrganizationsReconcileCreateArchivedErrorComponent
                | ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsReconcileCreateColorErrorComponent
                | ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent
                | ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent
                | ApiV1OrganizationsReconcileCreateCriticalityErrorComponent
                | ApiV1OrganizationsReconcileCreateDebugModeErrorComponent
                | ApiV1OrganizationsReconcileCreateDescriptionErrorComponent
                | ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent
                | ApiV1OrganizationsReconcileCreateDomainsErrorComponent
                | ApiV1OrganizationsReconcileCreateEmailsErrorComponent
                | ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent
                | ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent
                | ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsReconcileCreateKindErrorComponent
                | ApiV1OrganizationsReconcileCreateLabelsErrorComponent
                | ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsReconcileCreateLegalNameErrorComponent
                | ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent
                | ApiV1OrganizationsReconcileCreateNameErrorComponent
                | ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent
                | ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent
                | ApiV1OrganizationsReconcileCreatePriorityErrorComponent
                | ApiV1OrganizationsReconcileCreateProviderErrorComponent
                | ApiV1OrganizationsReconcileCreateProviderIdErrorComponent
                | ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent
                | ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsReconcileCreateScopeErrorComponent
                | ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent
                | ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1OrganizationsReconcileCreateSloTargetErrorComponent
                | ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent
                | ApiV1OrganizationsReconcileCreateSlugErrorComponent
                | ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsReconcileCreateUrlsErrorComponent
                | ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_0 = (
                        ApiV1OrganizationsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_1 = (
                        ApiV1OrganizationsReconcileCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_2 = (
                        ApiV1OrganizationsReconcileCreateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_3 = (
                        ApiV1OrganizationsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_4 = (
                        ApiV1OrganizationsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_5 = (
                        ApiV1OrganizationsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_6 = (
                        ApiV1OrganizationsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_7 = (
                        ApiV1OrganizationsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_8 = (
                        ApiV1OrganizationsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_9 = (
                        ApiV1OrganizationsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_10 = (
                        ApiV1OrganizationsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_11 = (
                        ApiV1OrganizationsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_12 = (
                        ApiV1OrganizationsReconcileCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_13 = (
                        ApiV1OrganizationsReconcileCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_14 = (
                        ApiV1OrganizationsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_15 = (
                        ApiV1OrganizationsReconcileCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_16 = (
                        ApiV1OrganizationsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_17 = (
                        ApiV1OrganizationsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_18 = (
                        ApiV1OrganizationsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_19 = (
                        ApiV1OrganizationsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_20 = (
                        ApiV1OrganizationsReconcileCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_21 = (
                        ApiV1OrganizationsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_22 = (
                        ApiV1OrganizationsReconcileCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_23 = (
                        ApiV1OrganizationsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_24 = (
                        ApiV1OrganizationsReconcileCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_25 = (
                        ApiV1OrganizationsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_26 = (
                        ApiV1OrganizationsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_27 = (
                        ApiV1OrganizationsReconcileCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_28 = (
                        ApiV1OrganizationsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_29 = (
                        ApiV1OrganizationsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_30 = (
                        ApiV1OrganizationsReconcileCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_31 = (
                        ApiV1OrganizationsReconcileCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_32 = (
                        ApiV1OrganizationsReconcileCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_33 = (
                        ApiV1OrganizationsReconcileCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_34 = (
                        ApiV1OrganizationsReconcileCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_35 = (
                        ApiV1OrganizationsReconcileCreateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_36 = (
                        ApiV1OrganizationsReconcileCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_37 = (
                        ApiV1OrganizationsReconcileCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_38 = (
                        ApiV1OrganizationsReconcileCreateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_39 = (
                        ApiV1OrganizationsReconcileCreateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_40 = (
                        ApiV1OrganizationsReconcileCreateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_41 = (
                        ApiV1OrganizationsReconcileCreateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_42 = (
                        ApiV1OrganizationsReconcileCreateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_43 = (
                        ApiV1OrganizationsReconcileCreateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_44 = (
                        ApiV1OrganizationsReconcileCreateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_45 = (
                        ApiV1OrganizationsReconcileCreateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_46 = (
                        ApiV1OrganizationsReconcileCreateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_47 = (
                        ApiV1OrganizationsReconcileCreateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_48 = (
                        ApiV1OrganizationsReconcileCreateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_49 = (
                        ApiV1OrganizationsReconcileCreateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_50 = (
                        ApiV1OrganizationsReconcileCreateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_51 = (
                        ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_52 = (
                        ApiV1OrganizationsReconcileCreateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_53 = (
                        ApiV1OrganizationsReconcileCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_54 = (
                        ApiV1OrganizationsReconcileCreateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_55 = (
                        ApiV1OrganizationsReconcileCreateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_56 = (
                        ApiV1OrganizationsReconcileCreateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_57 = (
                        ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_58 = (
                        ApiV1OrganizationsReconcileCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_59 = (
                        ApiV1OrganizationsReconcileCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_60 = (
                        ApiV1OrganizationsReconcileCreateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_61 = (
                        ApiV1OrganizationsReconcileCreateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_62 = (
                        ApiV1OrganizationsReconcileCreateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_63 = (
                        ApiV1OrganizationsReconcileCreateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_64 = (
                        ApiV1OrganizationsReconcileCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_65 = (
                        ApiV1OrganizationsReconcileCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_66 = (
                        ApiV1OrganizationsReconcileCreateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_67 = (
                        ApiV1OrganizationsReconcileCreateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_68 = (
                        ApiV1OrganizationsReconcileCreateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_69 = (
                        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_70 = (
                        ApiV1OrganizationsReconcileCreateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_71 = (
                        ApiV1OrganizationsReconcileCreateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_72 = (
                        ApiV1OrganizationsReconcileCreateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_73 = (
                        ApiV1OrganizationsReconcileCreateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_74 = (
                        ApiV1OrganizationsReconcileCreateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_75 = (
                        ApiV1OrganizationsReconcileCreateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_76 = (
                        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_77 = (
                        ApiV1OrganizationsReconcileCreateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_78 = (
                        ApiV1OrganizationsReconcileCreateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_79 = (
                        ApiV1OrganizationsReconcileCreateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_80 = (
                        ApiV1OrganizationsReconcileCreateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_81 = (
                        ApiV1OrganizationsReconcileCreateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_82 = (
                        ApiV1OrganizationsReconcileCreateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_83 = (
                        ApiV1OrganizationsReconcileCreateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_84 = (
                        ApiV1OrganizationsReconcileCreateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_85 = (
                        ApiV1OrganizationsReconcileCreateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_86 = (
                        ApiV1OrganizationsReconcileCreateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_87 = (
                        ApiV1OrganizationsReconcileCreateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_88 = (
                        ApiV1OrganizationsReconcileCreateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_89 = (
                        ApiV1OrganizationsReconcileCreateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_90 = (
                        ApiV1OrganizationsReconcileCreateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_91 = (
                        ApiV1OrganizationsReconcileCreateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_92 = (
                        ApiV1OrganizationsReconcileCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_93 = (
                        ApiV1OrganizationsReconcileCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_94 = (
                        ApiV1OrganizationsReconcileCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_95 = (
                        ApiV1OrganizationsReconcileCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_reconcile_create_error_type_96 = (
                        ApiV1OrganizationsReconcileCreateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_reconcile_create_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_reconcile_create_error_type_97 = (
                    ApiV1OrganizationsReconcileCreateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_reconcile_create_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_reconcile_create_validation_error.additional_properties = d
        return api_v1_organizations_reconcile_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
