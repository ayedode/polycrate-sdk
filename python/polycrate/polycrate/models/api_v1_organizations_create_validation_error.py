from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_create_active_error_component import ApiV1OrganizationsCreateActiveErrorComponent
    from ..models.api_v1_organizations_create_actual_availability_error_component import (
        ApiV1OrganizationsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_create_alias_error_component import ApiV1OrganizationsCreateAliasErrorComponent
    from ..models.api_v1_organizations_create_annotations_error_component import (
        ApiV1OrganizationsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_create_archived_at_error_component import (
        ApiV1OrganizationsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_create_archived_by_error_component import (
        ApiV1OrganizationsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_create_archived_error_component import (
        ApiV1OrganizationsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_create_archived_reason_error_component import (
        ApiV1OrganizationsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_endpoint_count_error_component import (
        ApiV1OrganizationsCreateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_lb_count_error_component import (
        ApiV1OrganizationsCreateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_logs_30d_error_component import (
        ApiV1OrganizationsCreateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_member_active_count_error_component import (
        ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_member_count_error_component import (
        ApiV1OrganizationsCreateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_s3_object_count_error_component import (
        ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_total_product_cost_error_component import (
        ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_volume_count_error_component import (
        ApiV1OrganizationsCreateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_cached_workspace_count_error_component import (
        ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_create_color_error_component import ApiV1OrganizationsCreateColorErrorComponent
    from ..models.api_v1_organizations_create_created_by_component_error_component import (
        ApiV1OrganizationsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_create_created_by_user_error_component import (
        ApiV1OrganizationsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_create_criticality_error_component import (
        ApiV1OrganizationsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_create_debug_mode_error_component import (
        ApiV1OrganizationsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_create_description_error_component import (
        ApiV1OrganizationsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_create_discovery_enabled_error_component import (
        ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_create_display_name_error_component import (
        ApiV1OrganizationsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_create_domains_error_component import (
        ApiV1OrganizationsCreateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_create_emails_error_component import ApiV1OrganizationsCreateEmailsErrorComponent
    from ..models.api_v1_organizations_create_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_create_endpoint_monitors_error_component import (
        ApiV1OrganizationsCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_create_gitlab_group_id_error_component import (
        ApiV1OrganizationsCreateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_gitlab_group_url_error_component import (
        ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_create_grafana_org_id_error_component import (
        ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_group_id_error_component import (
        ApiV1OrganizationsCreateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_project_id_error_component import (
        ApiV1OrganizationsCreateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_create_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_create_icon_content_type_error_component import (
        ApiV1OrganizationsCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_create_icon_filename_error_component import (
        ApiV1OrganizationsCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_create_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_create_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_create_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_create_kind_error_component import ApiV1OrganizationsCreateKindErrorComponent
    from ..models.api_v1_organizations_create_labels_error_component import ApiV1OrganizationsCreateLabelsErrorComponent
    from ..models.api_v1_organizations_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_create_legal_name_error_component import (
        ApiV1OrganizationsCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_create_loopback_org_id_error_component import (
        ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_loopback_project_id_error_component import (
        ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_managed_by_content_type_error_component import (
        ApiV1OrganizationsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_create_managed_by_object_id_error_component import (
        ApiV1OrganizationsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_modified_by_user_error_component import (
        ApiV1OrganizationsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_create_name_error_component import ApiV1OrganizationsCreateNameErrorComponent
    from ..models.api_v1_organizations_create_non_field_errors_error_component import (
        ApiV1OrganizationsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_create_observability_metrics_error_component import (
        ApiV1OrganizationsCreateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_create_owner_id_error_component import (
        ApiV1OrganizationsCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_platform_dns_record_created_error_component import (
        ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_create_platform_service_error_component import (
        ApiV1OrganizationsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_create_priority_error_component import (
        ApiV1OrganizationsCreatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_create_provider_error_component import (
        ApiV1OrganizationsCreateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_create_provider_id_error_component import (
        ApiV1OrganizationsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_provider_reference_error_component import (
        ApiV1OrganizationsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_create_reconciliation_enabled_error_component import (
        ApiV1OrganizationsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_create_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_create_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_create_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_create_scope_error_component import ApiV1OrganizationsCreateScopeErrorComponent
    from ..models.api_v1_organizations_create_sla_availability_error_component import (
        ApiV1OrganizationsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_create_sla_target_error_component import (
        ApiV1OrganizationsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_create_sla_window_days_error_component import (
        ApiV1OrganizationsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_create_slo_availability_error_component import (
        ApiV1OrganizationsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_create_slo_target_error_component import (
        ApiV1OrganizationsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_create_slo_window_days_error_component import (
        ApiV1OrganizationsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_create_slug_error_component import ApiV1OrganizationsCreateSlugErrorComponent
    from ..models.api_v1_organizations_create_target_availability_error_component import (
        ApiV1OrganizationsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_create_unified_harbor_credential_error_component import (
        ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_create_upstream_organization_id_error_component import (
        ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_upstream_system_id_error_component import (
        ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_create_urls_error_component import ApiV1OrganizationsCreateUrlsErrorComponent
    from ..models.api_v1_organizations_create_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsCreateValidationError")


@_attrs_define
class ApiV1OrganizationsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsCreateActiveErrorComponent |
            ApiV1OrganizationsCreateActualAvailabilityErrorComponent | ApiV1OrganizationsCreateAliasErrorComponent |
            ApiV1OrganizationsCreateAnnotationsErrorComponent |
            ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsCreateArchivedAtErrorComponent | ApiV1OrganizationsCreateArchivedByErrorComponent |
            ApiV1OrganizationsCreateArchivedErrorComponent | ApiV1OrganizationsCreateArchivedReasonErrorComponent |
            ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsCreateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsCreateCachedLbCountErrorComponent |
            ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsCreateCachedLogs30DErrorComponent |
            ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsCreateCachedMemberCountErrorComponent |
            ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsCreateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent | ApiV1OrganizationsCreateColorErrorComponent |
            ApiV1OrganizationsCreateCreatedByComponentErrorComponent | ApiV1OrganizationsCreateCreatedByUserErrorComponent |
            ApiV1OrganizationsCreateCriticalityErrorComponent | ApiV1OrganizationsCreateDebugModeErrorComponent |
            ApiV1OrganizationsCreateDescriptionErrorComponent | ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsCreateDisplayNameErrorComponent | ApiV1OrganizationsCreateDomainsErrorComponent |
            ApiV1OrganizationsCreateEmailsErrorComponent | ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsCreateEndpointMonitorsErrorComponent | ApiV1OrganizationsCreateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent | ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsCreateHarborGroupIdErrorComponent | ApiV1OrganizationsCreateHarborProjectIdErrorComponent |
            ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsCreateIconContentTypeErrorComponent | ApiV1OrganizationsCreateIconFilenameErrorComponent |
            ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent | ApiV1OrganizationsCreateKindErrorComponent |
            ApiV1OrganizationsCreateLabelsErrorComponent |
            ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsCreateLegalNameErrorComponent | ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsCreateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsCreateManagedByObjectIdErrorComponent | ApiV1OrganizationsCreateModifiedByUserErrorComponent |
            ApiV1OrganizationsCreateNameErrorComponent | ApiV1OrganizationsCreateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsCreateObservabilityMetricsErrorComponent | ApiV1OrganizationsCreateOwnerIdErrorComponent |
            ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsCreatePlatformServiceErrorComponent | ApiV1OrganizationsCreatePriorityErrorComponent |
            ApiV1OrganizationsCreateProviderErrorComponent | ApiV1OrganizationsCreateProviderIdErrorComponent |
            ApiV1OrganizationsCreateProviderReferenceErrorComponent |
            ApiV1OrganizationsCreateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent | ApiV1OrganizationsCreateScopeErrorComponent |
            ApiV1OrganizationsCreateSlaAvailabilityErrorComponent | ApiV1OrganizationsCreateSlaTargetErrorComponent |
            ApiV1OrganizationsCreateSlaWindowDaysErrorComponent | ApiV1OrganizationsCreateSloAvailabilityErrorComponent |
            ApiV1OrganizationsCreateSloTargetErrorComponent | ApiV1OrganizationsCreateSloWindowDaysErrorComponent |
            ApiV1OrganizationsCreateSlugErrorComponent | ApiV1OrganizationsCreateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent | ApiV1OrganizationsCreateUrlsErrorComponent |
            ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsCreateActiveErrorComponent
        | ApiV1OrganizationsCreateActualAvailabilityErrorComponent
        | ApiV1OrganizationsCreateAliasErrorComponent
        | ApiV1OrganizationsCreateAnnotationsErrorComponent
        | ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsCreateArchivedAtErrorComponent
        | ApiV1OrganizationsCreateArchivedByErrorComponent
        | ApiV1OrganizationsCreateArchivedErrorComponent
        | ApiV1OrganizationsCreateArchivedReasonErrorComponent
        | ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsCreateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsCreateCachedLbCountErrorComponent
        | ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsCreateCachedLogs30DErrorComponent
        | ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsCreateCachedMemberCountErrorComponent
        | ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsCreateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsCreateColorErrorComponent
        | ApiV1OrganizationsCreateCreatedByComponentErrorComponent
        | ApiV1OrganizationsCreateCreatedByUserErrorComponent
        | ApiV1OrganizationsCreateCriticalityErrorComponent
        | ApiV1OrganizationsCreateDebugModeErrorComponent
        | ApiV1OrganizationsCreateDescriptionErrorComponent
        | ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsCreateDisplayNameErrorComponent
        | ApiV1OrganizationsCreateDomainsErrorComponent
        | ApiV1OrganizationsCreateEmailsErrorComponent
        | ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsCreateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsCreateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsCreateHarborGroupIdErrorComponent
        | ApiV1OrganizationsCreateHarborProjectIdErrorComponent
        | ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsCreateIconContentTypeErrorComponent
        | ApiV1OrganizationsCreateIconFilenameErrorComponent
        | ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsCreateKindErrorComponent
        | ApiV1OrganizationsCreateLabelsErrorComponent
        | ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsCreateLegalNameErrorComponent
        | ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsCreateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsCreateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsCreateModifiedByUserErrorComponent
        | ApiV1OrganizationsCreateNameErrorComponent
        | ApiV1OrganizationsCreateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsCreateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsCreateOwnerIdErrorComponent
        | ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsCreatePlatformServiceErrorComponent
        | ApiV1OrganizationsCreatePriorityErrorComponent
        | ApiV1OrganizationsCreateProviderErrorComponent
        | ApiV1OrganizationsCreateProviderIdErrorComponent
        | ApiV1OrganizationsCreateProviderReferenceErrorComponent
        | ApiV1OrganizationsCreateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsCreateScopeErrorComponent
        | ApiV1OrganizationsCreateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsCreateSlaTargetErrorComponent
        | ApiV1OrganizationsCreateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsCreateSloAvailabilityErrorComponent
        | ApiV1OrganizationsCreateSloTargetErrorComponent
        | ApiV1OrganizationsCreateSloWindowDaysErrorComponent
        | ApiV1OrganizationsCreateSlugErrorComponent
        | ApiV1OrganizationsCreateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsCreateUrlsErrorComponent
        | ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_create_active_error_component import (
            ApiV1OrganizationsCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_create_actual_availability_error_component import (
            ApiV1OrganizationsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_alias_error_component import (
            ApiV1OrganizationsCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_create_annotations_error_component import (
            ApiV1OrganizationsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_at_error_component import (
            ApiV1OrganizationsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_by_error_component import (
            ApiV1OrganizationsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_error_component import (
            ApiV1OrganizationsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_reason_error_component import (
            ApiV1OrganizationsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_count_error_component import (
            ApiV1OrganizationsCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_member_count_error_component import (
            ApiV1OrganizationsCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_volume_count_error_component import (
            ApiV1OrganizationsCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_color_error_component import (
            ApiV1OrganizationsCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_create_created_by_component_error_component import (
            ApiV1OrganizationsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_create_created_by_user_error_component import (
            ApiV1OrganizationsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_create_criticality_error_component import (
            ApiV1OrganizationsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_create_debug_mode_error_component import (
            ApiV1OrganizationsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_create_description_error_component import (
            ApiV1OrganizationsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_create_discovery_enabled_error_component import (
            ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_display_name_error_component import (
            ApiV1OrganizationsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_domains_error_component import (
            ApiV1OrganizationsCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_create_emails_error_component import (
            ApiV1OrganizationsCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_create_grafana_org_id_error_component import (
            ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_group_id_error_component import (
            ApiV1OrganizationsCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_project_id_error_component import (
            ApiV1OrganizationsCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_icon_content_type_error_component import (
            ApiV1OrganizationsCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_create_icon_filename_error_component import (
            ApiV1OrganizationsCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_kind_error_component import ApiV1OrganizationsCreateKindErrorComponent
        from ..models.api_v1_organizations_create_labels_error_component import (
            ApiV1OrganizationsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_create_legal_name_error_component import (
            ApiV1OrganizationsCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_loopback_org_id_error_component import (
            ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_loopback_project_id_error_component import (
            ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_modified_by_user_error_component import (
            ApiV1OrganizationsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_create_name_error_component import ApiV1OrganizationsCreateNameErrorComponent
        from ..models.api_v1_organizations_create_non_field_errors_error_component import (
            ApiV1OrganizationsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_create_observability_metrics_error_component import (
            ApiV1OrganizationsCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_create_owner_id_error_component import (
            ApiV1OrganizationsCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_create_platform_service_error_component import (
            ApiV1OrganizationsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_create_priority_error_component import (
            ApiV1OrganizationsCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_error_component import (
            ApiV1OrganizationsCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_id_error_component import (
            ApiV1OrganizationsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_reference_error_component import (
            ApiV1OrganizationsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_scope_error_component import (
            ApiV1OrganizationsCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_availability_error_component import (
            ApiV1OrganizationsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_target_error_component import (
            ApiV1OrganizationsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_window_days_error_component import (
            ApiV1OrganizationsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_availability_error_component import (
            ApiV1OrganizationsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_target_error_component import (
            ApiV1OrganizationsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_window_days_error_component import (
            ApiV1OrganizationsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_create_slug_error_component import ApiV1OrganizationsCreateSlugErrorComponent
        from ..models.api_v1_organizations_create_target_availability_error_component import (
            ApiV1OrganizationsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_upstream_system_id_error_component import (
            ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_urls_error_component import ApiV1OrganizationsCreateUrlsErrorComponent
        from ..models.api_v1_organizations_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_create_active_error_component import (
            ApiV1OrganizationsCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_create_actual_availability_error_component import (
            ApiV1OrganizationsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_alias_error_component import (
            ApiV1OrganizationsCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_create_annotations_error_component import (
            ApiV1OrganizationsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_at_error_component import (
            ApiV1OrganizationsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_by_error_component import (
            ApiV1OrganizationsCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_error_component import (
            ApiV1OrganizationsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_create_archived_reason_error_component import (
            ApiV1OrganizationsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_count_error_component import (
            ApiV1OrganizationsCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_member_count_error_component import (
            ApiV1OrganizationsCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_volume_count_error_component import (
            ApiV1OrganizationsCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_create_color_error_component import (
            ApiV1OrganizationsCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_create_created_by_component_error_component import (
            ApiV1OrganizationsCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_create_created_by_user_error_component import (
            ApiV1OrganizationsCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_create_criticality_error_component import (
            ApiV1OrganizationsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_create_debug_mode_error_component import (
            ApiV1OrganizationsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_create_description_error_component import (
            ApiV1OrganizationsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_create_discovery_enabled_error_component import (
            ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_display_name_error_component import (
            ApiV1OrganizationsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_domains_error_component import (
            ApiV1OrganizationsCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_create_emails_error_component import (
            ApiV1OrganizationsCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_create_endpoint_monitors_error_component import (
            ApiV1OrganizationsCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_organizations_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_create_grafana_org_id_error_component import (
            ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_group_id_error_component import (
            ApiV1OrganizationsCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_project_id_error_component import (
            ApiV1OrganizationsCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_create_icon_content_type_error_component import (
            ApiV1OrganizationsCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_create_icon_filename_error_component import (
            ApiV1OrganizationsCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_kind_error_component import ApiV1OrganizationsCreateKindErrorComponent
        from ..models.api_v1_organizations_create_labels_error_component import (
            ApiV1OrganizationsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_create_legal_name_error_component import (
            ApiV1OrganizationsCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_loopback_org_id_error_component import (
            ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_loopback_project_id_error_component import (
            ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_modified_by_user_error_component import (
            ApiV1OrganizationsCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_create_name_error_component import ApiV1OrganizationsCreateNameErrorComponent
        from ..models.api_v1_organizations_create_non_field_errors_error_component import (
            ApiV1OrganizationsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_create_observability_metrics_error_component import (
            ApiV1OrganizationsCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_create_owner_id_error_component import (
            ApiV1OrganizationsCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_create_platform_service_error_component import (
            ApiV1OrganizationsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_create_priority_error_component import (
            ApiV1OrganizationsCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_error_component import (
            ApiV1OrganizationsCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_id_error_component import (
            ApiV1OrganizationsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_provider_reference_error_component import (
            ApiV1OrganizationsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_create_scope_error_component import (
            ApiV1OrganizationsCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_availability_error_component import (
            ApiV1OrganizationsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_target_error_component import (
            ApiV1OrganizationsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_create_sla_window_days_error_component import (
            ApiV1OrganizationsCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_availability_error_component import (
            ApiV1OrganizationsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_target_error_component import (
            ApiV1OrganizationsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_create_slo_window_days_error_component import (
            ApiV1OrganizationsCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_create_slug_error_component import ApiV1OrganizationsCreateSlugErrorComponent
        from ..models.api_v1_organizations_create_target_availability_error_component import (
            ApiV1OrganizationsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_upstream_system_id_error_component import (
            ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_create_urls_error_component import ApiV1OrganizationsCreateUrlsErrorComponent
        from ..models.api_v1_organizations_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsCreateActiveErrorComponent
                | ApiV1OrganizationsCreateActualAvailabilityErrorComponent
                | ApiV1OrganizationsCreateAliasErrorComponent
                | ApiV1OrganizationsCreateAnnotationsErrorComponent
                | ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsCreateArchivedAtErrorComponent
                | ApiV1OrganizationsCreateArchivedByErrorComponent
                | ApiV1OrganizationsCreateArchivedErrorComponent
                | ApiV1OrganizationsCreateArchivedReasonErrorComponent
                | ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsCreateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsCreateCachedLbCountErrorComponent
                | ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsCreateCachedLogs30DErrorComponent
                | ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsCreateCachedMemberCountErrorComponent
                | ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsCreateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsCreateColorErrorComponent
                | ApiV1OrganizationsCreateCreatedByComponentErrorComponent
                | ApiV1OrganizationsCreateCreatedByUserErrorComponent
                | ApiV1OrganizationsCreateCriticalityErrorComponent
                | ApiV1OrganizationsCreateDebugModeErrorComponent
                | ApiV1OrganizationsCreateDescriptionErrorComponent
                | ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsCreateDisplayNameErrorComponent
                | ApiV1OrganizationsCreateDomainsErrorComponent
                | ApiV1OrganizationsCreateEmailsErrorComponent
                | ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsCreateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsCreateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsCreateHarborGroupIdErrorComponent
                | ApiV1OrganizationsCreateHarborProjectIdErrorComponent
                | ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsCreateIconContentTypeErrorComponent
                | ApiV1OrganizationsCreateIconFilenameErrorComponent
                | ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsCreateKindErrorComponent
                | ApiV1OrganizationsCreateLabelsErrorComponent
                | ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsCreateLegalNameErrorComponent
                | ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsCreateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsCreateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsCreateModifiedByUserErrorComponent
                | ApiV1OrganizationsCreateNameErrorComponent
                | ApiV1OrganizationsCreateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsCreateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsCreateOwnerIdErrorComponent
                | ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsCreatePlatformServiceErrorComponent
                | ApiV1OrganizationsCreatePriorityErrorComponent
                | ApiV1OrganizationsCreateProviderErrorComponent
                | ApiV1OrganizationsCreateProviderIdErrorComponent
                | ApiV1OrganizationsCreateProviderReferenceErrorComponent
                | ApiV1OrganizationsCreateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsCreateScopeErrorComponent
                | ApiV1OrganizationsCreateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsCreateSlaTargetErrorComponent
                | ApiV1OrganizationsCreateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsCreateSloAvailabilityErrorComponent
                | ApiV1OrganizationsCreateSloTargetErrorComponent
                | ApiV1OrganizationsCreateSloWindowDaysErrorComponent
                | ApiV1OrganizationsCreateSlugErrorComponent
                | ApiV1OrganizationsCreateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsCreateUrlsErrorComponent
                | ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_0 = (
                        ApiV1OrganizationsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_1 = (
                        ApiV1OrganizationsCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_2 = (
                        ApiV1OrganizationsCreateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_3 = (
                        ApiV1OrganizationsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_4 = (
                        ApiV1OrganizationsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_5 = (
                        ApiV1OrganizationsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_6 = (
                        ApiV1OrganizationsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_7 = (
                        ApiV1OrganizationsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_8 = (
                        ApiV1OrganizationsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_9 = (
                        ApiV1OrganizationsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_10 = (
                        ApiV1OrganizationsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_11 = (
                        ApiV1OrganizationsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_12 = (
                        ApiV1OrganizationsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_13 = (
                        ApiV1OrganizationsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_14 = (
                        ApiV1OrganizationsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_15 = (
                        ApiV1OrganizationsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_16 = (
                        ApiV1OrganizationsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_17 = (
                        ApiV1OrganizationsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_18 = (
                        ApiV1OrganizationsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_19 = (
                        ApiV1OrganizationsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_20 = (
                        ApiV1OrganizationsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_21 = (
                        ApiV1OrganizationsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_22 = (
                        ApiV1OrganizationsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_23 = (
                        ApiV1OrganizationsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_24 = (
                        ApiV1OrganizationsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_25 = (
                        ApiV1OrganizationsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_26 = (
                        ApiV1OrganizationsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_27 = (
                        ApiV1OrganizationsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_28 = (
                        ApiV1OrganizationsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_29 = (
                        ApiV1OrganizationsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_30 = (
                        ApiV1OrganizationsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_31 = (
                        ApiV1OrganizationsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_32 = (
                        ApiV1OrganizationsCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_33 = (
                        ApiV1OrganizationsCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_34 = (
                        ApiV1OrganizationsCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_35 = (
                        ApiV1OrganizationsCreateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_36 = (
                        ApiV1OrganizationsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_37 = (
                        ApiV1OrganizationsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_38 = (
                        ApiV1OrganizationsCreateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_39 = (
                        ApiV1OrganizationsCreateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_40 = (
                        ApiV1OrganizationsCreateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_41 = (
                        ApiV1OrganizationsCreateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_42 = (
                        ApiV1OrganizationsCreateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_43 = (
                        ApiV1OrganizationsCreateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_44 = (
                        ApiV1OrganizationsCreateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_45 = (
                        ApiV1OrganizationsCreateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_46 = (
                        ApiV1OrganizationsCreateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_47 = (
                        ApiV1OrganizationsCreateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_48 = (
                        ApiV1OrganizationsCreateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_49 = (
                        ApiV1OrganizationsCreateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_50 = (
                        ApiV1OrganizationsCreateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_51 = (
                        ApiV1OrganizationsCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_52 = (
                        ApiV1OrganizationsCreateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_53 = (
                        ApiV1OrganizationsCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_54 = (
                        ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_55 = (
                        ApiV1OrganizationsCreateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_56 = (
                        ApiV1OrganizationsCreateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_57 = (
                        ApiV1OrganizationsCreateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_58 = (
                        ApiV1OrganizationsCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_59 = (
                        ApiV1OrganizationsCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_60 = (
                        ApiV1OrganizationsCreateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_61 = (
                        ApiV1OrganizationsCreateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_62 = (
                        ApiV1OrganizationsCreateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_63 = (
                        ApiV1OrganizationsCreateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_64 = (
                        ApiV1OrganizationsCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_65 = (
                        ApiV1OrganizationsCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_66 = (
                        ApiV1OrganizationsCreateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_67 = (
                        ApiV1OrganizationsCreateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_68 = (
                        ApiV1OrganizationsCreateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_69 = (
                        ApiV1OrganizationsCreateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_70 = (
                        ApiV1OrganizationsCreateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_71 = (
                        ApiV1OrganizationsCreateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_72 = (
                        ApiV1OrganizationsCreateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_73 = (
                        ApiV1OrganizationsCreateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_74 = (
                        ApiV1OrganizationsCreateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_75 = (
                        ApiV1OrganizationsCreateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_76 = (
                        ApiV1OrganizationsCreateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_77 = (
                        ApiV1OrganizationsCreateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_78 = (
                        ApiV1OrganizationsCreateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_79 = (
                        ApiV1OrganizationsCreateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_80 = (
                        ApiV1OrganizationsCreateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_81 = (
                        ApiV1OrganizationsCreateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_82 = (
                        ApiV1OrganizationsCreateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_83 = (
                        ApiV1OrganizationsCreateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_84 = (
                        ApiV1OrganizationsCreateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_85 = (
                        ApiV1OrganizationsCreateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_86 = (
                        ApiV1OrganizationsCreateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_87 = (
                        ApiV1OrganizationsCreateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_88 = (
                        ApiV1OrganizationsCreateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_89 = (
                        ApiV1OrganizationsCreateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_90 = (
                        ApiV1OrganizationsCreateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_91 = (
                        ApiV1OrganizationsCreateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_92 = (
                        ApiV1OrganizationsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_93 = (
                        ApiV1OrganizationsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_94 = (
                        ApiV1OrganizationsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_95 = (
                        ApiV1OrganizationsCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_create_error_type_96 = (
                        ApiV1OrganizationsCreateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_create_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_create_error_type_97 = (
                    ApiV1OrganizationsCreateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_create_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_create_validation_error.additional_properties = d
        return api_v1_organizations_create_validation_error

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
