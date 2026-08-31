from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_update_active_error_component import ApiV1OrganizationsUpdateActiveErrorComponent
    from ..models.api_v1_organizations_update_actual_availability_error_component import (
        ApiV1OrganizationsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_update_alias_error_component import ApiV1OrganizationsUpdateAliasErrorComponent
    from ..models.api_v1_organizations_update_annotations_error_component import (
        ApiV1OrganizationsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_update_archived_at_error_component import (
        ApiV1OrganizationsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_update_archived_by_error_component import (
        ApiV1OrganizationsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_update_archived_error_component import (
        ApiV1OrganizationsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_update_archived_reason_error_component import (
        ApiV1OrganizationsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_endpoint_count_error_component import (
        ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_lb_count_error_component import (
        ApiV1OrganizationsUpdateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_logs_30d_error_component import (
        ApiV1OrganizationsUpdateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_member_active_count_error_component import (
        ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_member_count_error_component import (
        ApiV1OrganizationsUpdateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_s3_object_count_error_component import (
        ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_total_product_cost_error_component import (
        ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_volume_count_error_component import (
        ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_cached_workspace_count_error_component import (
        ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_update_color_error_component import ApiV1OrganizationsUpdateColorErrorComponent
    from ..models.api_v1_organizations_update_created_by_component_error_component import (
        ApiV1OrganizationsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_update_created_by_user_error_component import (
        ApiV1OrganizationsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_update_criticality_error_component import (
        ApiV1OrganizationsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_update_debug_mode_error_component import (
        ApiV1OrganizationsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_update_description_error_component import (
        ApiV1OrganizationsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_update_discovery_enabled_error_component import (
        ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_update_display_name_error_component import (
        ApiV1OrganizationsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_update_domains_error_component import (
        ApiV1OrganizationsUpdateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_update_emails_error_component import ApiV1OrganizationsUpdateEmailsErrorComponent
    from ..models.api_v1_organizations_update_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_update_endpoint_monitors_error_component import (
        ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_update_gitlab_group_id_error_component import (
        ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_gitlab_group_url_error_component import (
        ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_update_grafana_org_id_error_component import (
        ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_group_id_error_component import (
        ApiV1OrganizationsUpdateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_project_id_error_component import (
        ApiV1OrganizationsUpdateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_update_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_update_icon_content_type_error_component import (
        ApiV1OrganizationsUpdateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_update_icon_filename_error_component import (
        ApiV1OrganizationsUpdateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_update_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_update_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_update_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_update_kind_error_component import ApiV1OrganizationsUpdateKindErrorComponent
    from ..models.api_v1_organizations_update_labels_error_component import ApiV1OrganizationsUpdateLabelsErrorComponent
    from ..models.api_v1_organizations_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_update_legal_name_error_component import (
        ApiV1OrganizationsUpdateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_update_loopback_org_id_error_component import (
        ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_loopback_project_id_error_component import (
        ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_managed_by_content_type_error_component import (
        ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_update_managed_by_object_id_error_component import (
        ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_modified_by_user_error_component import (
        ApiV1OrganizationsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_update_name_error_component import ApiV1OrganizationsUpdateNameErrorComponent
    from ..models.api_v1_organizations_update_non_field_errors_error_component import (
        ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_update_observability_metrics_error_component import (
        ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_update_owner_id_error_component import (
        ApiV1OrganizationsUpdateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_platform_dns_record_created_error_component import (
        ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_update_platform_service_error_component import (
        ApiV1OrganizationsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_update_priority_error_component import (
        ApiV1OrganizationsUpdatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_update_provider_error_component import (
        ApiV1OrganizationsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_update_provider_id_error_component import (
        ApiV1OrganizationsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_provider_reference_error_component import (
        ApiV1OrganizationsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_update_reconciliation_enabled_error_component import (
        ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_update_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_update_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_update_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_update_scope_error_component import ApiV1OrganizationsUpdateScopeErrorComponent
    from ..models.api_v1_organizations_update_sla_availability_error_component import (
        ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_update_sla_target_error_component import (
        ApiV1OrganizationsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_update_sla_window_days_error_component import (
        ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_update_slo_availability_error_component import (
        ApiV1OrganizationsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_update_slo_target_error_component import (
        ApiV1OrganizationsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_update_slo_window_days_error_component import (
        ApiV1OrganizationsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_update_slug_error_component import ApiV1OrganizationsUpdateSlugErrorComponent
    from ..models.api_v1_organizations_update_target_availability_error_component import (
        ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_update_unified_harbor_credential_error_component import (
        ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_update_upstream_organization_id_error_component import (
        ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_upstream_system_id_error_component import (
        ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_update_urls_error_component import ApiV1OrganizationsUpdateUrlsErrorComponent
    from ..models.api_v1_organizations_update_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsUpdateValidationError")


@_attrs_define
class ApiV1OrganizationsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsUpdateActiveErrorComponent |
            ApiV1OrganizationsUpdateActualAvailabilityErrorComponent | ApiV1OrganizationsUpdateAliasErrorComponent |
            ApiV1OrganizationsUpdateAnnotationsErrorComponent |
            ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsUpdateArchivedAtErrorComponent | ApiV1OrganizationsUpdateArchivedByErrorComponent |
            ApiV1OrganizationsUpdateArchivedErrorComponent | ApiV1OrganizationsUpdateArchivedReasonErrorComponent |
            ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsUpdateCachedLbCountErrorComponent |
            ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsUpdateCachedLogs30DErrorComponent |
            ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsUpdateCachedMemberCountErrorComponent |
            ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent | ApiV1OrganizationsUpdateColorErrorComponent |
            ApiV1OrganizationsUpdateCreatedByComponentErrorComponent | ApiV1OrganizationsUpdateCreatedByUserErrorComponent |
            ApiV1OrganizationsUpdateCriticalityErrorComponent | ApiV1OrganizationsUpdateDebugModeErrorComponent |
            ApiV1OrganizationsUpdateDescriptionErrorComponent | ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsUpdateDisplayNameErrorComponent | ApiV1OrganizationsUpdateDomainsErrorComponent |
            ApiV1OrganizationsUpdateEmailsErrorComponent | ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent | ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent | ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsUpdateHarborGroupIdErrorComponent | ApiV1OrganizationsUpdateHarborProjectIdErrorComponent |
            ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsUpdateIconContentTypeErrorComponent | ApiV1OrganizationsUpdateIconFilenameErrorComponent |
            ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent | ApiV1OrganizationsUpdateKindErrorComponent |
            ApiV1OrganizationsUpdateLabelsErrorComponent |
            ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsUpdateLegalNameErrorComponent | ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent | ApiV1OrganizationsUpdateModifiedByUserErrorComponent |
            ApiV1OrganizationsUpdateNameErrorComponent | ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent | ApiV1OrganizationsUpdateOwnerIdErrorComponent |
            ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsUpdatePlatformServiceErrorComponent | ApiV1OrganizationsUpdatePriorityErrorComponent |
            ApiV1OrganizationsUpdateProviderErrorComponent | ApiV1OrganizationsUpdateProviderIdErrorComponent |
            ApiV1OrganizationsUpdateProviderReferenceErrorComponent |
            ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent | ApiV1OrganizationsUpdateScopeErrorComponent |
            ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent | ApiV1OrganizationsUpdateSlaTargetErrorComponent |
            ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent | ApiV1OrganizationsUpdateSloAvailabilityErrorComponent |
            ApiV1OrganizationsUpdateSloTargetErrorComponent | ApiV1OrganizationsUpdateSloWindowDaysErrorComponent |
            ApiV1OrganizationsUpdateSlugErrorComponent | ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent | ApiV1OrganizationsUpdateUrlsErrorComponent |
            ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsUpdateActiveErrorComponent
        | ApiV1OrganizationsUpdateActualAvailabilityErrorComponent
        | ApiV1OrganizationsUpdateAliasErrorComponent
        | ApiV1OrganizationsUpdateAnnotationsErrorComponent
        | ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsUpdateArchivedAtErrorComponent
        | ApiV1OrganizationsUpdateArchivedByErrorComponent
        | ApiV1OrganizationsUpdateArchivedErrorComponent
        | ApiV1OrganizationsUpdateArchivedReasonErrorComponent
        | ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsUpdateCachedLbCountErrorComponent
        | ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsUpdateCachedLogs30DErrorComponent
        | ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsUpdateCachedMemberCountErrorComponent
        | ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsUpdateColorErrorComponent
        | ApiV1OrganizationsUpdateCreatedByComponentErrorComponent
        | ApiV1OrganizationsUpdateCreatedByUserErrorComponent
        | ApiV1OrganizationsUpdateCriticalityErrorComponent
        | ApiV1OrganizationsUpdateDebugModeErrorComponent
        | ApiV1OrganizationsUpdateDescriptionErrorComponent
        | ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsUpdateDisplayNameErrorComponent
        | ApiV1OrganizationsUpdateDomainsErrorComponent
        | ApiV1OrganizationsUpdateEmailsErrorComponent
        | ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsUpdateHarborGroupIdErrorComponent
        | ApiV1OrganizationsUpdateHarborProjectIdErrorComponent
        | ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsUpdateIconContentTypeErrorComponent
        | ApiV1OrganizationsUpdateIconFilenameErrorComponent
        | ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsUpdateKindErrorComponent
        | ApiV1OrganizationsUpdateLabelsErrorComponent
        | ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsUpdateLegalNameErrorComponent
        | ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsUpdateModifiedByUserErrorComponent
        | ApiV1OrganizationsUpdateNameErrorComponent
        | ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsUpdateOwnerIdErrorComponent
        | ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsUpdatePlatformServiceErrorComponent
        | ApiV1OrganizationsUpdatePriorityErrorComponent
        | ApiV1OrganizationsUpdateProviderErrorComponent
        | ApiV1OrganizationsUpdateProviderIdErrorComponent
        | ApiV1OrganizationsUpdateProviderReferenceErrorComponent
        | ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsUpdateScopeErrorComponent
        | ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsUpdateSlaTargetErrorComponent
        | ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsUpdateSloAvailabilityErrorComponent
        | ApiV1OrganizationsUpdateSloTargetErrorComponent
        | ApiV1OrganizationsUpdateSloWindowDaysErrorComponent
        | ApiV1OrganizationsUpdateSlugErrorComponent
        | ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsUpdateUrlsErrorComponent
        | ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_update_active_error_component import (
            ApiV1OrganizationsUpdateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_update_actual_availability_error_component import (
            ApiV1OrganizationsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_alias_error_component import (
            ApiV1OrganizationsUpdateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_update_annotations_error_component import (
            ApiV1OrganizationsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_at_error_component import (
            ApiV1OrganizationsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_by_error_component import (
            ApiV1OrganizationsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_error_component import (
            ApiV1OrganizationsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_reason_error_component import (
            ApiV1OrganizationsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_endpoint_count_error_component import (
            ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_count_error_component import (
            ApiV1OrganizationsUpdateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_logs_30d_error_component import (
            ApiV1OrganizationsUpdateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_member_active_count_error_component import (
            ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_member_count_error_component import (
            ApiV1OrganizationsUpdateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_object_count_error_component import (
            ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_total_product_cost_error_component import (
            ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_volume_count_error_component import (
            ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_workspace_count_error_component import (
            ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_color_error_component import (
            ApiV1OrganizationsUpdateColorErrorComponent,
        )
        from ..models.api_v1_organizations_update_created_by_component_error_component import (
            ApiV1OrganizationsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_update_created_by_user_error_component import (
            ApiV1OrganizationsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_update_criticality_error_component import (
            ApiV1OrganizationsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_update_debug_mode_error_component import (
            ApiV1OrganizationsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_update_description_error_component import (
            ApiV1OrganizationsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_update_discovery_enabled_error_component import (
            ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_display_name_error_component import (
            ApiV1OrganizationsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_domains_error_component import (
            ApiV1OrganizationsUpdateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_update_emails_error_component import (
            ApiV1OrganizationsUpdateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_update_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_update_gitlab_group_id_error_component import (
            ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_gitlab_group_url_error_component import (
            ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_update_grafana_org_id_error_component import (
            ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_group_id_error_component import (
            ApiV1OrganizationsUpdateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_project_id_error_component import (
            ApiV1OrganizationsUpdateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_icon_content_type_error_component import (
            ApiV1OrganizationsUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_update_icon_filename_error_component import (
            ApiV1OrganizationsUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_kind_error_component import ApiV1OrganizationsUpdateKindErrorComponent
        from ..models.api_v1_organizations_update_labels_error_component import (
            ApiV1OrganizationsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_update_legal_name_error_component import (
            ApiV1OrganizationsUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_loopback_org_id_error_component import (
            ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_loopback_project_id_error_component import (
            ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_managed_by_content_type_error_component import (
            ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_update_managed_by_object_id_error_component import (
            ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_modified_by_user_error_component import (
            ApiV1OrganizationsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_update_name_error_component import ApiV1OrganizationsUpdateNameErrorComponent
        from ..models.api_v1_organizations_update_non_field_errors_error_component import (
            ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_update_observability_metrics_error_component import (
            ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_update_owner_id_error_component import (
            ApiV1OrganizationsUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_platform_dns_record_created_error_component import (
            ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_update_platform_service_error_component import (
            ApiV1OrganizationsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_update_priority_error_component import (
            ApiV1OrganizationsUpdatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_error_component import (
            ApiV1OrganizationsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_id_error_component import (
            ApiV1OrganizationsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_reference_error_component import (
            ApiV1OrganizationsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_update_reconciliation_enabled_error_component import (
            ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_scope_error_component import (
            ApiV1OrganizationsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_availability_error_component import (
            ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_target_error_component import (
            ApiV1OrganizationsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_window_days_error_component import (
            ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_availability_error_component import (
            ApiV1OrganizationsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_target_error_component import (
            ApiV1OrganizationsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_window_days_error_component import (
            ApiV1OrganizationsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_update_slug_error_component import ApiV1OrganizationsUpdateSlugErrorComponent
        from ..models.api_v1_organizations_update_target_availability_error_component import (
            ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_unified_harbor_credential_error_component import (
            ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_update_upstream_organization_id_error_component import (
            ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_upstream_system_id_error_component import (
            ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_urls_error_component import ApiV1OrganizationsUpdateUrlsErrorComponent
        from ..models.api_v1_organizations_update_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_update_active_error_component import (
            ApiV1OrganizationsUpdateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_update_actual_availability_error_component import (
            ApiV1OrganizationsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_alias_error_component import (
            ApiV1OrganizationsUpdateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_update_annotations_error_component import (
            ApiV1OrganizationsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_at_error_component import (
            ApiV1OrganizationsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_by_error_component import (
            ApiV1OrganizationsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_error_component import (
            ApiV1OrganizationsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_update_archived_reason_error_component import (
            ApiV1OrganizationsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_endpoint_count_error_component import (
            ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_count_error_component import (
            ApiV1OrganizationsUpdateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_logs_30d_error_component import (
            ApiV1OrganizationsUpdateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_member_active_count_error_component import (
            ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_member_count_error_component import (
            ApiV1OrganizationsUpdateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_object_count_error_component import (
            ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_total_product_cost_error_component import (
            ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_volume_count_error_component import (
            ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_cached_workspace_count_error_component import (
            ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_update_color_error_component import (
            ApiV1OrganizationsUpdateColorErrorComponent,
        )
        from ..models.api_v1_organizations_update_created_by_component_error_component import (
            ApiV1OrganizationsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_update_created_by_user_error_component import (
            ApiV1OrganizationsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_update_criticality_error_component import (
            ApiV1OrganizationsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_update_debug_mode_error_component import (
            ApiV1OrganizationsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_update_description_error_component import (
            ApiV1OrganizationsUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_update_discovery_enabled_error_component import (
            ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_display_name_error_component import (
            ApiV1OrganizationsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_domains_error_component import (
            ApiV1OrganizationsUpdateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_update_emails_error_component import (
            ApiV1OrganizationsUpdateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_update_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_update_endpoint_monitors_error_component import (
            ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_organizations_update_gitlab_group_id_error_component import (
            ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_gitlab_group_url_error_component import (
            ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_update_grafana_org_id_error_component import (
            ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_group_id_error_component import (
            ApiV1OrganizationsUpdateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_project_id_error_component import (
            ApiV1OrganizationsUpdateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_update_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_update_icon_content_type_error_component import (
            ApiV1OrganizationsUpdateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_update_icon_filename_error_component import (
            ApiV1OrganizationsUpdateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_kind_error_component import ApiV1OrganizationsUpdateKindErrorComponent
        from ..models.api_v1_organizations_update_labels_error_component import (
            ApiV1OrganizationsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_update_legal_name_error_component import (
            ApiV1OrganizationsUpdateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_loopback_org_id_error_component import (
            ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_loopback_project_id_error_component import (
            ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_managed_by_content_type_error_component import (
            ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_update_managed_by_object_id_error_component import (
            ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_modified_by_user_error_component import (
            ApiV1OrganizationsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_update_name_error_component import ApiV1OrganizationsUpdateNameErrorComponent
        from ..models.api_v1_organizations_update_non_field_errors_error_component import (
            ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_update_observability_metrics_error_component import (
            ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_update_owner_id_error_component import (
            ApiV1OrganizationsUpdateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_platform_dns_record_created_error_component import (
            ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_update_platform_service_error_component import (
            ApiV1OrganizationsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_update_priority_error_component import (
            ApiV1OrganizationsUpdatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_error_component import (
            ApiV1OrganizationsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_id_error_component import (
            ApiV1OrganizationsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_provider_reference_error_component import (
            ApiV1OrganizationsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_update_reconciliation_enabled_error_component import (
            ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_update_scope_error_component import (
            ApiV1OrganizationsUpdateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_availability_error_component import (
            ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_target_error_component import (
            ApiV1OrganizationsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_update_sla_window_days_error_component import (
            ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_availability_error_component import (
            ApiV1OrganizationsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_target_error_component import (
            ApiV1OrganizationsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_update_slo_window_days_error_component import (
            ApiV1OrganizationsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_update_slug_error_component import ApiV1OrganizationsUpdateSlugErrorComponent
        from ..models.api_v1_organizations_update_target_availability_error_component import (
            ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_update_unified_harbor_credential_error_component import (
            ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_update_upstream_organization_id_error_component import (
            ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_upstream_system_id_error_component import (
            ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_update_urls_error_component import ApiV1OrganizationsUpdateUrlsErrorComponent
        from ..models.api_v1_organizations_update_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsUpdateActiveErrorComponent
                | ApiV1OrganizationsUpdateActualAvailabilityErrorComponent
                | ApiV1OrganizationsUpdateAliasErrorComponent
                | ApiV1OrganizationsUpdateAnnotationsErrorComponent
                | ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsUpdateArchivedAtErrorComponent
                | ApiV1OrganizationsUpdateArchivedByErrorComponent
                | ApiV1OrganizationsUpdateArchivedErrorComponent
                | ApiV1OrganizationsUpdateArchivedReasonErrorComponent
                | ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsUpdateCachedLbCountErrorComponent
                | ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsUpdateCachedLogs30DErrorComponent
                | ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsUpdateCachedMemberCountErrorComponent
                | ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsUpdateColorErrorComponent
                | ApiV1OrganizationsUpdateCreatedByComponentErrorComponent
                | ApiV1OrganizationsUpdateCreatedByUserErrorComponent
                | ApiV1OrganizationsUpdateCriticalityErrorComponent
                | ApiV1OrganizationsUpdateDebugModeErrorComponent
                | ApiV1OrganizationsUpdateDescriptionErrorComponent
                | ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsUpdateDisplayNameErrorComponent
                | ApiV1OrganizationsUpdateDomainsErrorComponent
                | ApiV1OrganizationsUpdateEmailsErrorComponent
                | ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsUpdateHarborGroupIdErrorComponent
                | ApiV1OrganizationsUpdateHarborProjectIdErrorComponent
                | ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsUpdateIconContentTypeErrorComponent
                | ApiV1OrganizationsUpdateIconFilenameErrorComponent
                | ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsUpdateKindErrorComponent
                | ApiV1OrganizationsUpdateLabelsErrorComponent
                | ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsUpdateLegalNameErrorComponent
                | ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsUpdateModifiedByUserErrorComponent
                | ApiV1OrganizationsUpdateNameErrorComponent
                | ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsUpdateOwnerIdErrorComponent
                | ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsUpdatePlatformServiceErrorComponent
                | ApiV1OrganizationsUpdatePriorityErrorComponent
                | ApiV1OrganizationsUpdateProviderErrorComponent
                | ApiV1OrganizationsUpdateProviderIdErrorComponent
                | ApiV1OrganizationsUpdateProviderReferenceErrorComponent
                | ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsUpdateScopeErrorComponent
                | ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsUpdateSlaTargetErrorComponent
                | ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsUpdateSloAvailabilityErrorComponent
                | ApiV1OrganizationsUpdateSloTargetErrorComponent
                | ApiV1OrganizationsUpdateSloWindowDaysErrorComponent
                | ApiV1OrganizationsUpdateSlugErrorComponent
                | ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsUpdateUrlsErrorComponent
                | ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_0 = (
                        ApiV1OrganizationsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_1 = (
                        ApiV1OrganizationsUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_2 = (
                        ApiV1OrganizationsUpdateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_3 = (
                        ApiV1OrganizationsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_4 = (
                        ApiV1OrganizationsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_5 = (
                        ApiV1OrganizationsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_6 = (
                        ApiV1OrganizationsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_7 = (
                        ApiV1OrganizationsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_8 = (
                        ApiV1OrganizationsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_9 = (
                        ApiV1OrganizationsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_10 = (
                        ApiV1OrganizationsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_11 = (
                        ApiV1OrganizationsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_12 = (
                        ApiV1OrganizationsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_13 = (
                        ApiV1OrganizationsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_14 = (
                        ApiV1OrganizationsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_15 = (
                        ApiV1OrganizationsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_16 = (
                        ApiV1OrganizationsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_17 = (
                        ApiV1OrganizationsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_18 = (
                        ApiV1OrganizationsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_19 = (
                        ApiV1OrganizationsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_20 = (
                        ApiV1OrganizationsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_21 = (
                        ApiV1OrganizationsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_22 = (
                        ApiV1OrganizationsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_23 = (
                        ApiV1OrganizationsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_24 = (
                        ApiV1OrganizationsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_25 = (
                        ApiV1OrganizationsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_26 = (
                        ApiV1OrganizationsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_27 = (
                        ApiV1OrganizationsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_28 = (
                        ApiV1OrganizationsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_29 = (
                        ApiV1OrganizationsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_30 = (
                        ApiV1OrganizationsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_31 = (
                        ApiV1OrganizationsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_32 = (
                        ApiV1OrganizationsUpdateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_33 = (
                        ApiV1OrganizationsUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_34 = (
                        ApiV1OrganizationsUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_35 = (
                        ApiV1OrganizationsUpdateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_36 = (
                        ApiV1OrganizationsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_37 = (
                        ApiV1OrganizationsUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_38 = (
                        ApiV1OrganizationsUpdateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_39 = (
                        ApiV1OrganizationsUpdateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_40 = (
                        ApiV1OrganizationsUpdateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_41 = (
                        ApiV1OrganizationsUpdateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_42 = (
                        ApiV1OrganizationsUpdateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_43 = (
                        ApiV1OrganizationsUpdateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_44 = (
                        ApiV1OrganizationsUpdateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_45 = (
                        ApiV1OrganizationsUpdateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_46 = (
                        ApiV1OrganizationsUpdateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_47 = (
                        ApiV1OrganizationsUpdateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_48 = (
                        ApiV1OrganizationsUpdateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_49 = (
                        ApiV1OrganizationsUpdateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_50 = (
                        ApiV1OrganizationsUpdateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_51 = (
                        ApiV1OrganizationsUpdateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_52 = (
                        ApiV1OrganizationsUpdateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_53 = (
                        ApiV1OrganizationsUpdatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_54 = (
                        ApiV1OrganizationsUpdateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_55 = (
                        ApiV1OrganizationsUpdateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_56 = (
                        ApiV1OrganizationsUpdateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_57 = (
                        ApiV1OrganizationsUpdateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_58 = (
                        ApiV1OrganizationsUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_59 = (
                        ApiV1OrganizationsUpdateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_60 = (
                        ApiV1OrganizationsUpdateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_61 = (
                        ApiV1OrganizationsUpdateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_62 = (
                        ApiV1OrganizationsUpdateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_63 = (
                        ApiV1OrganizationsUpdateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_64 = (
                        ApiV1OrganizationsUpdateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_65 = (
                        ApiV1OrganizationsUpdateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_66 = (
                        ApiV1OrganizationsUpdateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_67 = (
                        ApiV1OrganizationsUpdateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_68 = (
                        ApiV1OrganizationsUpdateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_69 = (
                        ApiV1OrganizationsUpdateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_70 = (
                        ApiV1OrganizationsUpdateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_71 = (
                        ApiV1OrganizationsUpdateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_72 = (
                        ApiV1OrganizationsUpdateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_73 = (
                        ApiV1OrganizationsUpdateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_74 = (
                        ApiV1OrganizationsUpdateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_75 = (
                        ApiV1OrganizationsUpdateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_76 = (
                        ApiV1OrganizationsUpdateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_77 = (
                        ApiV1OrganizationsUpdateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_78 = (
                        ApiV1OrganizationsUpdateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_79 = (
                        ApiV1OrganizationsUpdateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_80 = (
                        ApiV1OrganizationsUpdateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_81 = (
                        ApiV1OrganizationsUpdateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_82 = (
                        ApiV1OrganizationsUpdateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_83 = (
                        ApiV1OrganizationsUpdateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_84 = (
                        ApiV1OrganizationsUpdateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_85 = (
                        ApiV1OrganizationsUpdateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_86 = (
                        ApiV1OrganizationsUpdateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_87 = (
                        ApiV1OrganizationsUpdateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_88 = (
                        ApiV1OrganizationsUpdateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_89 = (
                        ApiV1OrganizationsUpdateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_90 = (
                        ApiV1OrganizationsUpdateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_91 = (
                        ApiV1OrganizationsUpdateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_92 = (
                        ApiV1OrganizationsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_93 = (
                        ApiV1OrganizationsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_94 = (
                        ApiV1OrganizationsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_95 = (
                        ApiV1OrganizationsUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_update_error_type_96 = (
                        ApiV1OrganizationsUpdateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_update_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_update_error_type_97 = (
                    ApiV1OrganizationsUpdateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_update_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_update_validation_error.additional_properties = d
        return api_v1_organizations_update_validation_error

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
