from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_discover_create_active_error_component import (
        ApiV1OrganizationsDiscoverCreateActiveErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_actual_availability_error_component import (
        ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_alias_error_component import (
        ApiV1OrganizationsDiscoverCreateAliasErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_annotations_error_component import (
        ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_archived_at_error_component import (
        ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_archived_by_error_component import (
        ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_archived_error_component import (
        ApiV1OrganizationsDiscoverCreateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_archived_reason_error_component import (
        ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_endpoint_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_lb_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_logs_30d_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_member_active_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_member_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_s3_object_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_total_product_cost_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_volume_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_cached_workspace_count_error_component import (
        ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_color_error_component import (
        ApiV1OrganizationsDiscoverCreateColorErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_created_by_component_error_component import (
        ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_created_by_user_error_component import (
        ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_criticality_error_component import (
        ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_debug_mode_error_component import (
        ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_description_error_component import (
        ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_discovery_enabled_error_component import (
        ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_display_name_error_component import (
        ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_domains_error_component import (
        ApiV1OrganizationsDiscoverCreateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_emails_error_component import (
        ApiV1OrganizationsDiscoverCreateEmailsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_endpoint_monitors_error_component import (
        ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_gitlab_group_id_error_component import (
        ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_gitlab_group_url_error_component import (
        ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_grafana_org_id_error_component import (
        ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_group_id_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_project_id_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_icon_content_type_error_component import (
        ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_icon_filename_error_component import (
        ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_kind_error_component import (
        ApiV1OrganizationsDiscoverCreateKindErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_labels_error_component import (
        ApiV1OrganizationsDiscoverCreateLabelsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_legal_name_error_component import (
        ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_loopback_org_id_error_component import (
        ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_loopback_project_id_error_component import (
        ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_managed_by_content_type_error_component import (
        ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_managed_by_object_id_error_component import (
        ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_modified_by_user_error_component import (
        ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_name_error_component import (
        ApiV1OrganizationsDiscoverCreateNameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_non_field_errors_error_component import (
        ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_observability_metrics_error_component import (
        ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_owner_id_error_component import (
        ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_platform_dns_record_created_error_component import (
        ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_platform_service_error_component import (
        ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_priority_error_component import (
        ApiV1OrganizationsDiscoverCreatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_provider_error_component import (
        ApiV1OrganizationsDiscoverCreateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_provider_id_error_component import (
        ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_provider_reference_error_component import (
        ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_reconciliation_enabled_error_component import (
        ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_scope_error_component import (
        ApiV1OrganizationsDiscoverCreateScopeErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_sla_availability_error_component import (
        ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_sla_target_error_component import (
        ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_sla_window_days_error_component import (
        ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_slo_availability_error_component import (
        ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_slo_target_error_component import (
        ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_slo_window_days_error_component import (
        ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_slug_error_component import (
        ApiV1OrganizationsDiscoverCreateSlugErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_target_availability_error_component import (
        ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_unified_harbor_credential_error_component import (
        ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_upstream_organization_id_error_component import (
        ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_upstream_system_id_error_component import (
        ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_urls_error_component import (
        ApiV1OrganizationsDiscoverCreateUrlsErrorComponent,
    )
    from ..models.api_v1_organizations_discover_create_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsDiscoverCreateValidationError")


@_attrs_define
class ApiV1OrganizationsDiscoverCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsDiscoverCreateActiveErrorComponent |
            ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent |
            ApiV1OrganizationsDiscoverCreateAliasErrorComponent | ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent
            | ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent |
            ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent |
            ApiV1OrganizationsDiscoverCreateArchivedErrorComponent |
            ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent |
            ApiV1OrganizationsDiscoverCreateColorErrorComponent |
            ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent |
            ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent |
            ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent |
            ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent |
            ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent |
            ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent |
            ApiV1OrganizationsDiscoverCreateDomainsErrorComponent | ApiV1OrganizationsDiscoverCreateEmailsErrorComponent |
            ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent |
            ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent |
            ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent |
            ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent |
            ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent |
            ApiV1OrganizationsDiscoverCreateKindErrorComponent | ApiV1OrganizationsDiscoverCreateLabelsErrorComponent |
            ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent |
            ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent |
            ApiV1OrganizationsDiscoverCreateNameErrorComponent |
            ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent |
            ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent |
            ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent |
            ApiV1OrganizationsDiscoverCreatePriorityErrorComponent | ApiV1OrganizationsDiscoverCreateProviderErrorComponent
            | ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent |
            ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent |
            ApiV1OrganizationsDiscoverCreateScopeErrorComponent |
            ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent |
            ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent |
            ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent |
            ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent |
            ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent |
            ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent | ApiV1OrganizationsDiscoverCreateSlugErrorComponent
            | ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent |
            ApiV1OrganizationsDiscoverCreateUrlsErrorComponent |
            ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsDiscoverCreateActiveErrorComponent
        | ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent
        | ApiV1OrganizationsDiscoverCreateAliasErrorComponent
        | ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent
        | ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent
        | ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent
        | ApiV1OrganizationsDiscoverCreateArchivedErrorComponent
        | ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsDiscoverCreateColorErrorComponent
        | ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent
        | ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent
        | ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent
        | ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent
        | ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent
        | ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent
        | ApiV1OrganizationsDiscoverCreateDomainsErrorComponent
        | ApiV1OrganizationsDiscoverCreateEmailsErrorComponent
        | ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent
        | ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent
        | ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsDiscoverCreateKindErrorComponent
        | ApiV1OrganizationsDiscoverCreateLabelsErrorComponent
        | ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent
        | ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent
        | ApiV1OrganizationsDiscoverCreateNameErrorComponent
        | ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent
        | ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent
        | ApiV1OrganizationsDiscoverCreatePriorityErrorComponent
        | ApiV1OrganizationsDiscoverCreateProviderErrorComponent
        | ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent
        | ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsDiscoverCreateScopeErrorComponent
        | ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent
        | ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent
        | ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent
        | ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent
        | ApiV1OrganizationsDiscoverCreateSlugErrorComponent
        | ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsDiscoverCreateUrlsErrorComponent
        | ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_discover_create_active_error_component import (
            ApiV1OrganizationsDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_actual_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_alias_error_component import (
            ApiV1OrganizationsDiscoverCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_annotations_error_component import (
            ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_at_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_by_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_reason_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_member_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_volume_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_color_error_component import (
            ApiV1OrganizationsDiscoverCreateColorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_created_by_component_error_component import (
            ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_created_by_user_error_component import (
            ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_criticality_error_component import (
            ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_debug_mode_error_component import (
            ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_description_error_component import (
            ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_discovery_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_display_name_error_component import (
            ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_domains_error_component import (
            ApiV1OrganizationsDiscoverCreateDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_emails_error_component import (
            ApiV1OrganizationsDiscoverCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_grafana_org_id_error_component import (
            ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_group_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_project_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_icon_content_type_error_component import (
            ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_icon_filename_error_component import (
            ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_kind_error_component import (
            ApiV1OrganizationsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_labels_error_component import (
            ApiV1OrganizationsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_legal_name_error_component import (
            ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_loopback_org_id_error_component import (
            ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_loopback_project_id_error_component import (
            ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_modified_by_user_error_component import (
            ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_name_error_component import (
            ApiV1OrganizationsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_non_field_errors_error_component import (
            ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_observability_metrics_error_component import (
            ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_owner_id_error_component import (
            ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_platform_service_error_component import (
            ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_priority_error_component import (
            ApiV1OrganizationsDiscoverCreatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_id_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_reference_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_scope_error_component import (
            ApiV1OrganizationsDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_target_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_window_days_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_target_error_component import (
            ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_window_days_error_component import (
            ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slug_error_component import (
            ApiV1OrganizationsDiscoverCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_target_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_upstream_system_id_error_component import (
            ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_urls_error_component import (
            ApiV1OrganizationsDiscoverCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_discover_create_active_error_component import (
            ApiV1OrganizationsDiscoverCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_actual_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_alias_error_component import (
            ApiV1OrganizationsDiscoverCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_annotations_error_component import (
            ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_at_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_by_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_archived_reason_error_component import (
            ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_member_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_volume_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_color_error_component import (
            ApiV1OrganizationsDiscoverCreateColorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_created_by_component_error_component import (
            ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_created_by_user_error_component import (
            ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_criticality_error_component import (
            ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_debug_mode_error_component import (
            ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_description_error_component import (
            ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_discovery_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_display_name_error_component import (
            ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_domains_error_component import (
            ApiV1OrganizationsDiscoverCreateDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_emails_error_component import (
            ApiV1OrganizationsDiscoverCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_endpoint_monitors_error_component import (
            ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_grafana_org_id_error_component import (
            ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_group_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_project_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_icon_content_type_error_component import (
            ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_icon_filename_error_component import (
            ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_kind_error_component import (
            ApiV1OrganizationsDiscoverCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_labels_error_component import (
            ApiV1OrganizationsDiscoverCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_legal_name_error_component import (
            ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_loopback_org_id_error_component import (
            ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_loopback_project_id_error_component import (
            ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_modified_by_user_error_component import (
            ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_name_error_component import (
            ApiV1OrganizationsDiscoverCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_non_field_errors_error_component import (
            ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_observability_metrics_error_component import (
            ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_owner_id_error_component import (
            ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_platform_service_error_component import (
            ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_priority_error_component import (
            ApiV1OrganizationsDiscoverCreatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_id_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_provider_reference_error_component import (
            ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_scope_error_component import (
            ApiV1OrganizationsDiscoverCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_target_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_sla_window_days_error_component import (
            ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_target_error_component import (
            ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slo_window_days_error_component import (
            ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_slug_error_component import (
            ApiV1OrganizationsDiscoverCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_target_availability_error_component import (
            ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_upstream_system_id_error_component import (
            ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_urls_error_component import (
            ApiV1OrganizationsDiscoverCreateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_discover_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsDiscoverCreateActiveErrorComponent
                | ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent
                | ApiV1OrganizationsDiscoverCreateAliasErrorComponent
                | ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent
                | ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent
                | ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent
                | ApiV1OrganizationsDiscoverCreateArchivedErrorComponent
                | ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsDiscoverCreateColorErrorComponent
                | ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent
                | ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent
                | ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent
                | ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent
                | ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent
                | ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent
                | ApiV1OrganizationsDiscoverCreateDomainsErrorComponent
                | ApiV1OrganizationsDiscoverCreateEmailsErrorComponent
                | ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent
                | ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent
                | ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsDiscoverCreateKindErrorComponent
                | ApiV1OrganizationsDiscoverCreateLabelsErrorComponent
                | ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent
                | ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent
                | ApiV1OrganizationsDiscoverCreateNameErrorComponent
                | ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent
                | ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent
                | ApiV1OrganizationsDiscoverCreatePriorityErrorComponent
                | ApiV1OrganizationsDiscoverCreateProviderErrorComponent
                | ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent
                | ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsDiscoverCreateScopeErrorComponent
                | ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent
                | ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent
                | ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent
                | ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent
                | ApiV1OrganizationsDiscoverCreateSlugErrorComponent
                | ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsDiscoverCreateUrlsErrorComponent
                | ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_0 = (
                        ApiV1OrganizationsDiscoverCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_1 = (
                        ApiV1OrganizationsDiscoverCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_2 = (
                        ApiV1OrganizationsDiscoverCreateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_3 = (
                        ApiV1OrganizationsDiscoverCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_4 = (
                        ApiV1OrganizationsDiscoverCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_5 = (
                        ApiV1OrganizationsDiscoverCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_6 = (
                        ApiV1OrganizationsDiscoverCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_7 = (
                        ApiV1OrganizationsDiscoverCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_8 = (
                        ApiV1OrganizationsDiscoverCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_9 = (
                        ApiV1OrganizationsDiscoverCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_10 = (
                        ApiV1OrganizationsDiscoverCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_11 = (
                        ApiV1OrganizationsDiscoverCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_12 = (
                        ApiV1OrganizationsDiscoverCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_13 = (
                        ApiV1OrganizationsDiscoverCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_14 = (
                        ApiV1OrganizationsDiscoverCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_15 = (
                        ApiV1OrganizationsDiscoverCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_16 = (
                        ApiV1OrganizationsDiscoverCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_17 = (
                        ApiV1OrganizationsDiscoverCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_18 = (
                        ApiV1OrganizationsDiscoverCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_19 = (
                        ApiV1OrganizationsDiscoverCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_20 = (
                        ApiV1OrganizationsDiscoverCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_21 = (
                        ApiV1OrganizationsDiscoverCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_22 = (
                        ApiV1OrganizationsDiscoverCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_23 = (
                        ApiV1OrganizationsDiscoverCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_24 = (
                        ApiV1OrganizationsDiscoverCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_25 = (
                        ApiV1OrganizationsDiscoverCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_26 = (
                        ApiV1OrganizationsDiscoverCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_27 = (
                        ApiV1OrganizationsDiscoverCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_28 = (
                        ApiV1OrganizationsDiscoverCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_29 = (
                        ApiV1OrganizationsDiscoverCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_30 = (
                        ApiV1OrganizationsDiscoverCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_31 = (
                        ApiV1OrganizationsDiscoverCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_32 = (
                        ApiV1OrganizationsDiscoverCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_33 = (
                        ApiV1OrganizationsDiscoverCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_34 = (
                        ApiV1OrganizationsDiscoverCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_35 = (
                        ApiV1OrganizationsDiscoverCreateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_36 = (
                        ApiV1OrganizationsDiscoverCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_37 = (
                        ApiV1OrganizationsDiscoverCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_38 = (
                        ApiV1OrganizationsDiscoverCreateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_39 = (
                        ApiV1OrganizationsDiscoverCreateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_40 = (
                        ApiV1OrganizationsDiscoverCreateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_41 = (
                        ApiV1OrganizationsDiscoverCreateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_42 = (
                        ApiV1OrganizationsDiscoverCreateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_43 = (
                        ApiV1OrganizationsDiscoverCreateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_44 = (
                        ApiV1OrganizationsDiscoverCreateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_45 = (
                        ApiV1OrganizationsDiscoverCreateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_46 = (
                        ApiV1OrganizationsDiscoverCreateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_47 = (
                        ApiV1OrganizationsDiscoverCreateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_48 = (
                        ApiV1OrganizationsDiscoverCreateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_49 = (
                        ApiV1OrganizationsDiscoverCreateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_50 = (
                        ApiV1OrganizationsDiscoverCreateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_51 = (
                        ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_52 = (
                        ApiV1OrganizationsDiscoverCreateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_53 = (
                        ApiV1OrganizationsDiscoverCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_54 = (
                        ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_55 = (
                        ApiV1OrganizationsDiscoverCreateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_56 = (
                        ApiV1OrganizationsDiscoverCreateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_57 = (
                        ApiV1OrganizationsDiscoverCreateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_58 = (
                        ApiV1OrganizationsDiscoverCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_59 = (
                        ApiV1OrganizationsDiscoverCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_60 = (
                        ApiV1OrganizationsDiscoverCreateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_61 = (
                        ApiV1OrganizationsDiscoverCreateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_62 = (
                        ApiV1OrganizationsDiscoverCreateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_63 = (
                        ApiV1OrganizationsDiscoverCreateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_64 = (
                        ApiV1OrganizationsDiscoverCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_65 = (
                        ApiV1OrganizationsDiscoverCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_66 = (
                        ApiV1OrganizationsDiscoverCreateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_67 = (
                        ApiV1OrganizationsDiscoverCreateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_68 = (
                        ApiV1OrganizationsDiscoverCreateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_69 = (
                        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_70 = (
                        ApiV1OrganizationsDiscoverCreateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_71 = (
                        ApiV1OrganizationsDiscoverCreateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_72 = (
                        ApiV1OrganizationsDiscoverCreateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_73 = (
                        ApiV1OrganizationsDiscoverCreateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_74 = (
                        ApiV1OrganizationsDiscoverCreateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_75 = (
                        ApiV1OrganizationsDiscoverCreateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_76 = (
                        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_77 = (
                        ApiV1OrganizationsDiscoverCreateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_78 = (
                        ApiV1OrganizationsDiscoverCreateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_79 = (
                        ApiV1OrganizationsDiscoverCreateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_80 = (
                        ApiV1OrganizationsDiscoverCreateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_81 = (
                        ApiV1OrganizationsDiscoverCreateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_82 = (
                        ApiV1OrganizationsDiscoverCreateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_83 = (
                        ApiV1OrganizationsDiscoverCreateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_84 = (
                        ApiV1OrganizationsDiscoverCreateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_85 = (
                        ApiV1OrganizationsDiscoverCreateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_86 = (
                        ApiV1OrganizationsDiscoverCreateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_87 = (
                        ApiV1OrganizationsDiscoverCreateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_88 = (
                        ApiV1OrganizationsDiscoverCreateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_89 = (
                        ApiV1OrganizationsDiscoverCreateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_90 = (
                        ApiV1OrganizationsDiscoverCreateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_91 = (
                        ApiV1OrganizationsDiscoverCreateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_92 = (
                        ApiV1OrganizationsDiscoverCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_93 = (
                        ApiV1OrganizationsDiscoverCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_94 = (
                        ApiV1OrganizationsDiscoverCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_95 = (
                        ApiV1OrganizationsDiscoverCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_discover_create_error_type_96 = (
                        ApiV1OrganizationsDiscoverCreateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_discover_create_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_discover_create_error_type_97 = (
                    ApiV1OrganizationsDiscoverCreateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_discover_create_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_discover_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_discover_create_validation_error.additional_properties = d
        return api_v1_organizations_discover_create_validation_error

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
