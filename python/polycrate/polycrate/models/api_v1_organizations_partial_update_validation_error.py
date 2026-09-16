from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_partial_update_active_error_component import (
        ApiV1OrganizationsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_actual_availability_error_component import (
        ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_alias_error_component import (
        ApiV1OrganizationsPartialUpdateAliasErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_annotations_error_component import (
        ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_archived_at_error_component import (
        ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_archived_by_error_component import (
        ApiV1OrganizationsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_archived_error_component import (
        ApiV1OrganizationsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_archived_reason_error_component import (
        ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_endpoint_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_lb_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_logs_30d_error_component import (
        ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_member_active_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_member_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_s3_object_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_total_product_cost_error_component import (
        ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_volume_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_cached_workspace_count_error_component import (
        ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_color_error_component import (
        ApiV1OrganizationsPartialUpdateColorErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_created_by_component_error_component import (
        ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_created_by_user_error_component import (
        ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_criticality_error_component import (
        ApiV1OrganizationsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_debug_mode_error_component import (
        ApiV1OrganizationsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_description_error_component import (
        ApiV1OrganizationsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_discovery_enabled_error_component import (
        ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_display_name_error_component import (
        ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_domains_error_component import (
        ApiV1OrganizationsPartialUpdateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_emails_error_component import (
        ApiV1OrganizationsPartialUpdateEmailsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_endpoint_monitors_error_component import (
        ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_gitlab_group_id_error_component import (
        ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_gitlab_group_url_error_component import (
        ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_grafana_org_id_error_component import (
        ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_group_id_error_component import (
        ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_project_id_error_component import (
        ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_icon_content_type_error_component import (
        ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_icon_filename_error_component import (
        ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_kind_error_component import (
        ApiV1OrganizationsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_labels_error_component import (
        ApiV1OrganizationsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_legal_name_error_component import (
        ApiV1OrganizationsPartialUpdateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_loopback_org_id_error_component import (
        ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_loopback_project_id_error_component import (
        ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_managed_by_content_type_error_component import (
        ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_managed_by_object_id_error_component import (
        ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_modified_by_user_error_component import (
        ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_name_error_component import (
        ApiV1OrganizationsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_non_field_errors_error_component import (
        ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_observability_metrics_error_component import (
        ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_owner_id_error_component import (
        ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_platform_dns_record_created_error_component import (
        ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_platform_service_error_component import (
        ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_priority_error_component import (
        ApiV1OrganizationsPartialUpdatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_provider_error_component import (
        ApiV1OrganizationsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_provider_id_error_component import (
        ApiV1OrganizationsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_provider_reference_error_component import (
        ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_reconciliation_enabled_error_component import (
        ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_scope_error_component import (
        ApiV1OrganizationsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_sla_availability_error_component import (
        ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_sla_target_error_component import (
        ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_sla_window_days_error_component import (
        ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_slo_availability_error_component import (
        ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_slo_target_error_component import (
        ApiV1OrganizationsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_slo_window_days_error_component import (
        ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_slug_error_component import (
        ApiV1OrganizationsPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_target_availability_error_component import (
        ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_unified_harbor_credential_error_component import (
        ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_upstream_organization_id_error_component import (
        ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_upstream_system_id_error_component import (
        ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_urls_error_component import (
        ApiV1OrganizationsPartialUpdateUrlsErrorComponent,
    )
    from ..models.api_v1_organizations_partial_update_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsPartialUpdateValidationError")


@_attrs_define
class ApiV1OrganizationsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsPartialUpdateActiveErrorComponent |
            ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1OrganizationsPartialUpdateAliasErrorComponent | ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent |
            ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent |
            ApiV1OrganizationsPartialUpdateArchivedByErrorComponent | ApiV1OrganizationsPartialUpdateArchivedErrorComponent
            | ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent |
            ApiV1OrganizationsPartialUpdateColorErrorComponent |
            ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent |
            ApiV1OrganizationsPartialUpdateCriticalityErrorComponent |
            ApiV1OrganizationsPartialUpdateDebugModeErrorComponent |
            ApiV1OrganizationsPartialUpdateDescriptionErrorComponent |
            ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent | ApiV1OrganizationsPartialUpdateDomainsErrorComponent
            | ApiV1OrganizationsPartialUpdateEmailsErrorComponent |
            ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent |
            ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent |
            ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent |
            ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent |
            ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent |
            ApiV1OrganizationsPartialUpdateKindErrorComponent | ApiV1OrganizationsPartialUpdateLabelsErrorComponent |
            ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsPartialUpdateLegalNameErrorComponent |
            ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent | ApiV1OrganizationsPartialUpdateNameErrorComponent
            | ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent |
            ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent |
            ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent |
            ApiV1OrganizationsPartialUpdatePriorityErrorComponent | ApiV1OrganizationsPartialUpdateProviderErrorComponent |
            ApiV1OrganizationsPartialUpdateProviderIdErrorComponent |
            ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent |
            ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent |
            ApiV1OrganizationsPartialUpdateScopeErrorComponent |
            ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent |
            ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1OrganizationsPartialUpdateSloTargetErrorComponent |
            ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent | ApiV1OrganizationsPartialUpdateSlugErrorComponent |
            ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent |
            ApiV1OrganizationsPartialUpdateUrlsErrorComponent |
            ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsPartialUpdateActiveErrorComponent
        | ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1OrganizationsPartialUpdateAliasErrorComponent
        | ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent
        | ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent
        | ApiV1OrganizationsPartialUpdateArchivedByErrorComponent
        | ApiV1OrganizationsPartialUpdateArchivedErrorComponent
        | ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsPartialUpdateColorErrorComponent
        | ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent
        | ApiV1OrganizationsPartialUpdateCriticalityErrorComponent
        | ApiV1OrganizationsPartialUpdateDebugModeErrorComponent
        | ApiV1OrganizationsPartialUpdateDescriptionErrorComponent
        | ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent
        | ApiV1OrganizationsPartialUpdateDomainsErrorComponent
        | ApiV1OrganizationsPartialUpdateEmailsErrorComponent
        | ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent
        | ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent
        | ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsPartialUpdateKindErrorComponent
        | ApiV1OrganizationsPartialUpdateLabelsErrorComponent
        | ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsPartialUpdateLegalNameErrorComponent
        | ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent
        | ApiV1OrganizationsPartialUpdateNameErrorComponent
        | ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent
        | ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent
        | ApiV1OrganizationsPartialUpdatePriorityErrorComponent
        | ApiV1OrganizationsPartialUpdateProviderErrorComponent
        | ApiV1OrganizationsPartialUpdateProviderIdErrorComponent
        | ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent
        | ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsPartialUpdateScopeErrorComponent
        | ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent
        | ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1OrganizationsPartialUpdateSloTargetErrorComponent
        | ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1OrganizationsPartialUpdateSlugErrorComponent
        | ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsPartialUpdateUrlsErrorComponent
        | ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_partial_update_active_error_component import (
            ApiV1OrganizationsPartialUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_actual_availability_error_component import (
            ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_alias_error_component import (
            ApiV1OrganizationsPartialUpdateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_annotations_error_component import (
            ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_at_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_by_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_reason_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_endpoint_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_logs_30d_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_member_active_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_member_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_object_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_total_product_cost_error_component import (
            ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_volume_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_workspace_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_color_error_component import (
            ApiV1OrganizationsPartialUpdateColorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_created_by_component_error_component import (
            ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_created_by_user_error_component import (
            ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_criticality_error_component import (
            ApiV1OrganizationsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_debug_mode_error_component import (
            ApiV1OrganizationsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_description_error_component import (
            ApiV1OrganizationsPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_discovery_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_display_name_error_component import (
            ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_domains_error_component import (
            ApiV1OrganizationsPartialUpdateDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_emails_error_component import (
            ApiV1OrganizationsPartialUpdateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_gitlab_group_id_error_component import (
            ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_gitlab_group_url_error_component import (
            ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_grafana_org_id_error_component import (
            ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_group_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_project_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_icon_content_type_error_component import (
            ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_icon_filename_error_component import (
            ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_kind_error_component import (
            ApiV1OrganizationsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_labels_error_component import (
            ApiV1OrganizationsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_legal_name_error_component import (
            ApiV1OrganizationsPartialUpdateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_loopback_org_id_error_component import (
            ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_loopback_project_id_error_component import (
            ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_managed_by_content_type_error_component import (
            ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_managed_by_object_id_error_component import (
            ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_modified_by_user_error_component import (
            ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_name_error_component import (
            ApiV1OrganizationsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_non_field_errors_error_component import (
            ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_observability_metrics_error_component import (
            ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_owner_id_error_component import (
            ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_platform_dns_record_created_error_component import (
            ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_platform_service_error_component import (
            ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_priority_error_component import (
            ApiV1OrganizationsPartialUpdatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_error_component import (
            ApiV1OrganizationsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_id_error_component import (
            ApiV1OrganizationsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_reference_error_component import (
            ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_reconciliation_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_scope_error_component import (
            ApiV1OrganizationsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_availability_error_component import (
            ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_target_error_component import (
            ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_window_days_error_component import (
            ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_availability_error_component import (
            ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_target_error_component import (
            ApiV1OrganizationsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_window_days_error_component import (
            ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slug_error_component import (
            ApiV1OrganizationsPartialUpdateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_target_availability_error_component import (
            ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_unified_harbor_credential_error_component import (
            ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_upstream_organization_id_error_component import (
            ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_upstream_system_id_error_component import (
            ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_urls_error_component import (
            ApiV1OrganizationsPartialUpdateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_partial_update_active_error_component import (
            ApiV1OrganizationsPartialUpdateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_actual_availability_error_component import (
            ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_alias_error_component import (
            ApiV1OrganizationsPartialUpdateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_annotations_error_component import (
            ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_at_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_by_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_archived_reason_error_component import (
            ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_endpoint_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_logs_30d_error_component import (
            ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_member_active_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_member_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_object_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_total_product_cost_error_component import (
            ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_volume_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_cached_workspace_count_error_component import (
            ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_color_error_component import (
            ApiV1OrganizationsPartialUpdateColorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_created_by_component_error_component import (
            ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_created_by_user_error_component import (
            ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_criticality_error_component import (
            ApiV1OrganizationsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_debug_mode_error_component import (
            ApiV1OrganizationsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_description_error_component import (
            ApiV1OrganizationsPartialUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_discovery_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_display_name_error_component import (
            ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_domains_error_component import (
            ApiV1OrganizationsPartialUpdateDomainsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_emails_error_component import (
            ApiV1OrganizationsPartialUpdateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_endpoint_monitors_error_component import (
            ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_gitlab_group_id_error_component import (
            ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_gitlab_group_url_error_component import (
            ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_grafana_org_id_error_component import (
            ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_group_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_project_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_icon_content_type_error_component import (
            ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_icon_filename_error_component import (
            ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_kind_error_component import (
            ApiV1OrganizationsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_labels_error_component import (
            ApiV1OrganizationsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_legal_name_error_component import (
            ApiV1OrganizationsPartialUpdateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_loopback_org_id_error_component import (
            ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_loopback_project_id_error_component import (
            ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_managed_by_content_type_error_component import (
            ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_managed_by_object_id_error_component import (
            ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_modified_by_user_error_component import (
            ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_name_error_component import (
            ApiV1OrganizationsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_non_field_errors_error_component import (
            ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_observability_metrics_error_component import (
            ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_owner_id_error_component import (
            ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_platform_dns_record_created_error_component import (
            ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_platform_service_error_component import (
            ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_priority_error_component import (
            ApiV1OrganizationsPartialUpdatePriorityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_error_component import (
            ApiV1OrganizationsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_id_error_component import (
            ApiV1OrganizationsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_provider_reference_error_component import (
            ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_reconciliation_enabled_error_component import (
            ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_scope_error_component import (
            ApiV1OrganizationsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_availability_error_component import (
            ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_target_error_component import (
            ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_sla_window_days_error_component import (
            ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_availability_error_component import (
            ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_target_error_component import (
            ApiV1OrganizationsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slo_window_days_error_component import (
            ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_slug_error_component import (
            ApiV1OrganizationsPartialUpdateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_target_availability_error_component import (
            ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_unified_harbor_credential_error_component import (
            ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_upstream_organization_id_error_component import (
            ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_upstream_system_id_error_component import (
            ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_urls_error_component import (
            ApiV1OrganizationsPartialUpdateUrlsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_organizations_partial_update_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsPartialUpdateActiveErrorComponent
                | ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1OrganizationsPartialUpdateAliasErrorComponent
                | ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent
                | ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent
                | ApiV1OrganizationsPartialUpdateArchivedByErrorComponent
                | ApiV1OrganizationsPartialUpdateArchivedErrorComponent
                | ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsPartialUpdateColorErrorComponent
                | ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent
                | ApiV1OrganizationsPartialUpdateCriticalityErrorComponent
                | ApiV1OrganizationsPartialUpdateDebugModeErrorComponent
                | ApiV1OrganizationsPartialUpdateDescriptionErrorComponent
                | ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent
                | ApiV1OrganizationsPartialUpdateDomainsErrorComponent
                | ApiV1OrganizationsPartialUpdateEmailsErrorComponent
                | ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent
                | ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent
                | ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsPartialUpdateKindErrorComponent
                | ApiV1OrganizationsPartialUpdateLabelsErrorComponent
                | ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsPartialUpdateLegalNameErrorComponent
                | ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent
                | ApiV1OrganizationsPartialUpdateNameErrorComponent
                | ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent
                | ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent
                | ApiV1OrganizationsPartialUpdatePriorityErrorComponent
                | ApiV1OrganizationsPartialUpdateProviderErrorComponent
                | ApiV1OrganizationsPartialUpdateProviderIdErrorComponent
                | ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent
                | ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsPartialUpdateScopeErrorComponent
                | ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent
                | ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1OrganizationsPartialUpdateSloTargetErrorComponent
                | ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1OrganizationsPartialUpdateSlugErrorComponent
                | ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsPartialUpdateUrlsErrorComponent
                | ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_0 = (
                        ApiV1OrganizationsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_1 = (
                        ApiV1OrganizationsPartialUpdateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_2 = (
                        ApiV1OrganizationsPartialUpdateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_3 = (
                        ApiV1OrganizationsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_4 = (
                        ApiV1OrganizationsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_5 = (
                        ApiV1OrganizationsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_6 = (
                        ApiV1OrganizationsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_7 = (
                        ApiV1OrganizationsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_8 = (
                        ApiV1OrganizationsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_9 = (
                        ApiV1OrganizationsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_10 = (
                        ApiV1OrganizationsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_11 = (
                        ApiV1OrganizationsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_12 = (
                        ApiV1OrganizationsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_13 = (
                        ApiV1OrganizationsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_14 = (
                        ApiV1OrganizationsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_15 = (
                        ApiV1OrganizationsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_16 = (
                        ApiV1OrganizationsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_17 = (
                        ApiV1OrganizationsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_18 = (
                        ApiV1OrganizationsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_19 = (
                        ApiV1OrganizationsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_20 = (
                        ApiV1OrganizationsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_21 = (
                        ApiV1OrganizationsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_22 = (
                        ApiV1OrganizationsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_23 = (
                        ApiV1OrganizationsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_24 = (
                        ApiV1OrganizationsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_25 = (
                        ApiV1OrganizationsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_26 = (
                        ApiV1OrganizationsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_27 = (
                        ApiV1OrganizationsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_28 = (
                        ApiV1OrganizationsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_29 = (
                        ApiV1OrganizationsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_30 = (
                        ApiV1OrganizationsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_31 = (
                        ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_32 = (
                        ApiV1OrganizationsPartialUpdateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_33 = (
                        ApiV1OrganizationsPartialUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_34 = (
                        ApiV1OrganizationsPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_35 = (
                        ApiV1OrganizationsPartialUpdateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_36 = (
                        ApiV1OrganizationsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_37 = (
                        ApiV1OrganizationsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_38 = (
                        ApiV1OrganizationsPartialUpdateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_39 = (
                        ApiV1OrganizationsPartialUpdateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_40 = (
                        ApiV1OrganizationsPartialUpdateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_41 = (
                        ApiV1OrganizationsPartialUpdateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_42 = (
                        ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_43 = (
                        ApiV1OrganizationsPartialUpdateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_44 = (
                        ApiV1OrganizationsPartialUpdateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_45 = (
                        ApiV1OrganizationsPartialUpdateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_46 = (
                        ApiV1OrganizationsPartialUpdateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_47 = (
                        ApiV1OrganizationsPartialUpdateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_48 = (
                        ApiV1OrganizationsPartialUpdateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_49 = (
                        ApiV1OrganizationsPartialUpdateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_50 = (
                        ApiV1OrganizationsPartialUpdateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_51 = (
                        ApiV1OrganizationsPartialUpdateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_52 = (
                        ApiV1OrganizationsPartialUpdateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_53 = (
                        ApiV1OrganizationsPartialUpdatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_54 = (
                        ApiV1OrganizationsPartialUpdateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_55 = (
                        ApiV1OrganizationsPartialUpdateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_56 = (
                        ApiV1OrganizationsPartialUpdateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_57 = (
                        ApiV1OrganizationsPartialUpdateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_58 = (
                        ApiV1OrganizationsPartialUpdateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_59 = (
                        ApiV1OrganizationsPartialUpdateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_60 = (
                        ApiV1OrganizationsPartialUpdateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_61 = (
                        ApiV1OrganizationsPartialUpdateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_62 = (
                        ApiV1OrganizationsPartialUpdateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_63 = (
                        ApiV1OrganizationsPartialUpdateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_64 = (
                        ApiV1OrganizationsPartialUpdateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_65 = (
                        ApiV1OrganizationsPartialUpdateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_66 = (
                        ApiV1OrganizationsPartialUpdateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_67 = (
                        ApiV1OrganizationsPartialUpdateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_68 = (
                        ApiV1OrganizationsPartialUpdateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_69 = (
                        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_70 = (
                        ApiV1OrganizationsPartialUpdateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_71 = (
                        ApiV1OrganizationsPartialUpdateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_72 = (
                        ApiV1OrganizationsPartialUpdateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_73 = (
                        ApiV1OrganizationsPartialUpdateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_74 = (
                        ApiV1OrganizationsPartialUpdateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_75 = (
                        ApiV1OrganizationsPartialUpdateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_76 = (
                        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_77 = (
                        ApiV1OrganizationsPartialUpdateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_78 = (
                        ApiV1OrganizationsPartialUpdateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_79 = (
                        ApiV1OrganizationsPartialUpdateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_80 = (
                        ApiV1OrganizationsPartialUpdateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_81 = (
                        ApiV1OrganizationsPartialUpdateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_82 = (
                        ApiV1OrganizationsPartialUpdateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_83 = (
                        ApiV1OrganizationsPartialUpdateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_84 = (
                        ApiV1OrganizationsPartialUpdateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_85 = (
                        ApiV1OrganizationsPartialUpdateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_86 = (
                        ApiV1OrganizationsPartialUpdateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_87 = (
                        ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_88 = (
                        ApiV1OrganizationsPartialUpdateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_89 = (
                        ApiV1OrganizationsPartialUpdateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_90 = (
                        ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_91 = (
                        ApiV1OrganizationsPartialUpdateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_92 = (
                        ApiV1OrganizationsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_93 = (
                        ApiV1OrganizationsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_94 = (
                        ApiV1OrganizationsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_95 = (
                        ApiV1OrganizationsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_partial_update_error_type_96 = (
                        ApiV1OrganizationsPartialUpdateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_partial_update_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_partial_update_error_type_97 = (
                    ApiV1OrganizationsPartialUpdateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_partial_update_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_partial_update_validation_error.additional_properties = d
        return api_v1_organizations_partial_update_validation_error

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
