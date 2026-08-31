from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_icon_upload_create_active_error_component import (
        ApiV1OrganizationsIconUploadCreateActiveErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_actual_availability_error_component import (
        ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_alias_error_component import (
        ApiV1OrganizationsIconUploadCreateAliasErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_annotations_error_component import (
        ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_archived_at_error_component import (
        ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_archived_by_error_component import (
        ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_archived_error_component import (
        ApiV1OrganizationsIconUploadCreateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_archived_reason_error_component import (
        ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_lb_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_logs_30d_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_member_active_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_member_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_s3_object_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_total_product_cost_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_volume_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_cached_workspace_count_error_component import (
        ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_color_error_component import (
        ApiV1OrganizationsIconUploadCreateColorErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_created_by_component_error_component import (
        ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_created_by_user_error_component import (
        ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_criticality_error_component import (
        ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_debug_mode_error_component import (
        ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_description_error_component import (
        ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_discovery_enabled_error_component import (
        ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_display_name_error_component import (
        ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_domains_error_component import (
        ApiV1OrganizationsIconUploadCreateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_emails_error_component import (
        ApiV1OrganizationsIconUploadCreateEmailsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_endpoint_monitors_error_component import (
        ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_gitlab_group_id_error_component import (
        ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_gitlab_group_url_error_component import (
        ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_grafana_org_id_error_component import (
        ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_group_id_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_project_id_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_icon_content_type_error_component import (
        ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_icon_filename_error_component import (
        ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_kind_error_component import (
        ApiV1OrganizationsIconUploadCreateKindErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_labels_error_component import (
        ApiV1OrganizationsIconUploadCreateLabelsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_legal_name_error_component import (
        ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_loopback_org_id_error_component import (
        ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_loopback_project_id_error_component import (
        ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_managed_by_content_type_error_component import (
        ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_managed_by_object_id_error_component import (
        ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_modified_by_user_error_component import (
        ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_name_error_component import (
        ApiV1OrganizationsIconUploadCreateNameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_non_field_errors_error_component import (
        ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_observability_metrics_error_component import (
        ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_owner_id_error_component import (
        ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_platform_dns_record_created_error_component import (
        ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_platform_service_error_component import (
        ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_priority_error_component import (
        ApiV1OrganizationsIconUploadCreatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_provider_error_component import (
        ApiV1OrganizationsIconUploadCreateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_provider_id_error_component import (
        ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_provider_reference_error_component import (
        ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_reconciliation_enabled_error_component import (
        ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_scope_error_component import (
        ApiV1OrganizationsIconUploadCreateScopeErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_sla_availability_error_component import (
        ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_sla_target_error_component import (
        ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_sla_window_days_error_component import (
        ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_slo_availability_error_component import (
        ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_slo_target_error_component import (
        ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_slo_window_days_error_component import (
        ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_slug_error_component import (
        ApiV1OrganizationsIconUploadCreateSlugErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_target_availability_error_component import (
        ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_unified_harbor_credential_error_component import (
        ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_upstream_organization_id_error_component import (
        ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_upstream_system_id_error_component import (
        ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_urls_error_component import (
        ApiV1OrganizationsIconUploadCreateUrlsErrorComponent,
    )
    from ..models.api_v1_organizations_icon_upload_create_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsIconUploadCreateValidationError")


@_attrs_define
class ApiV1OrganizationsIconUploadCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsIconUploadCreateActiveErrorComponent |
            ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent |
            ApiV1OrganizationsIconUploadCreateAliasErrorComponent |
            ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent |
            ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent |
            ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent |
            ApiV1OrganizationsIconUploadCreateArchivedErrorComponent |
            ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent |
            ApiV1OrganizationsIconUploadCreateColorErrorComponent |
            ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent |
            ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent |
            ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent |
            ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent |
            ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent |
            ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent |
            ApiV1OrganizationsIconUploadCreateDomainsErrorComponent | ApiV1OrganizationsIconUploadCreateEmailsErrorComponent
            | ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent |
            ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent |
            ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent |
            ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent |
            ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent |
            ApiV1OrganizationsIconUploadCreateKindErrorComponent | ApiV1OrganizationsIconUploadCreateLabelsErrorComponent |
            ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent |
            ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent |
            ApiV1OrganizationsIconUploadCreateNameErrorComponent |
            ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent |
            ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent |
            ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent |
            ApiV1OrganizationsIconUploadCreatePriorityErrorComponent |
            ApiV1OrganizationsIconUploadCreateProviderErrorComponent |
            ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent |
            ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent |
            ApiV1OrganizationsIconUploadCreateScopeErrorComponent |
            ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent |
            ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent |
            ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent |
            ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent |
            ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent |
            ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent |
            ApiV1OrganizationsIconUploadCreateSlugErrorComponent |
            ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent |
            ApiV1OrganizationsIconUploadCreateUrlsErrorComponent |
            ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsIconUploadCreateActiveErrorComponent
        | ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent
        | ApiV1OrganizationsIconUploadCreateAliasErrorComponent
        | ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent
        | ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent
        | ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent
        | ApiV1OrganizationsIconUploadCreateArchivedErrorComponent
        | ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsIconUploadCreateColorErrorComponent
        | ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent
        | ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent
        | ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent
        | ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent
        | ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent
        | ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent
        | ApiV1OrganizationsIconUploadCreateDomainsErrorComponent
        | ApiV1OrganizationsIconUploadCreateEmailsErrorComponent
        | ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent
        | ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent
        | ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsIconUploadCreateKindErrorComponent
        | ApiV1OrganizationsIconUploadCreateLabelsErrorComponent
        | ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent
        | ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent
        | ApiV1OrganizationsIconUploadCreateNameErrorComponent
        | ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent
        | ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent
        | ApiV1OrganizationsIconUploadCreatePriorityErrorComponent
        | ApiV1OrganizationsIconUploadCreateProviderErrorComponent
        | ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent
        | ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsIconUploadCreateScopeErrorComponent
        | ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent
        | ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent
        | ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent
        | ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent
        | ApiV1OrganizationsIconUploadCreateSlugErrorComponent
        | ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsIconUploadCreateUrlsErrorComponent
        | ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_icon_upload_create_active_error_component import (
            ApiV1OrganizationsIconUploadCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_actual_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_alias_error_component import (
            ApiV1OrganizationsIconUploadCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_annotations_error_component import (
            ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_at_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_by_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_reason_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_member_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_volume_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_color_error_component import (
            ApiV1OrganizationsIconUploadCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_created_by_component_error_component import (
            ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_created_by_user_error_component import (
            ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_criticality_error_component import (
            ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_debug_mode_error_component import (
            ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_description_error_component import (
            ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_discovery_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_display_name_error_component import (
            ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_domains_error_component import (
            ApiV1OrganizationsIconUploadCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_emails_error_component import (
            ApiV1OrganizationsIconUploadCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_grafana_org_id_error_component import (
            ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_group_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_project_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_icon_content_type_error_component import (
            ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_icon_filename_error_component import (
            ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_kind_error_component import (
            ApiV1OrganizationsIconUploadCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_labels_error_component import (
            ApiV1OrganizationsIconUploadCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_legal_name_error_component import (
            ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_loopback_org_id_error_component import (
            ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_loopback_project_id_error_component import (
            ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_modified_by_user_error_component import (
            ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_name_error_component import (
            ApiV1OrganizationsIconUploadCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_non_field_errors_error_component import (
            ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_observability_metrics_error_component import (
            ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_owner_id_error_component import (
            ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_platform_service_error_component import (
            ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_priority_error_component import (
            ApiV1OrganizationsIconUploadCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_id_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_reference_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_scope_error_component import (
            ApiV1OrganizationsIconUploadCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_target_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_window_days_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_target_error_component import (
            ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_window_days_error_component import (
            ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slug_error_component import (
            ApiV1OrganizationsIconUploadCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_target_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_upstream_system_id_error_component import (
            ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_urls_error_component import (
            ApiV1OrganizationsIconUploadCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_icon_upload_create_active_error_component import (
            ApiV1OrganizationsIconUploadCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_actual_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_alias_error_component import (
            ApiV1OrganizationsIconUploadCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_annotations_error_component import (
            ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_at_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_by_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_archived_reason_error_component import (
            ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_member_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_volume_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_color_error_component import (
            ApiV1OrganizationsIconUploadCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_created_by_component_error_component import (
            ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_created_by_user_error_component import (
            ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_criticality_error_component import (
            ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_debug_mode_error_component import (
            ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_description_error_component import (
            ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_discovery_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_display_name_error_component import (
            ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_domains_error_component import (
            ApiV1OrganizationsIconUploadCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_emails_error_component import (
            ApiV1OrganizationsIconUploadCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_endpoint_monitors_error_component import (
            ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_grafana_org_id_error_component import (
            ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_group_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_project_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_icon_content_type_error_component import (
            ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_icon_filename_error_component import (
            ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_kind_error_component import (
            ApiV1OrganizationsIconUploadCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_labels_error_component import (
            ApiV1OrganizationsIconUploadCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_legal_name_error_component import (
            ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_loopback_org_id_error_component import (
            ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_loopback_project_id_error_component import (
            ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_modified_by_user_error_component import (
            ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_name_error_component import (
            ApiV1OrganizationsIconUploadCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_non_field_errors_error_component import (
            ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_observability_metrics_error_component import (
            ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_owner_id_error_component import (
            ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_platform_service_error_component import (
            ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_priority_error_component import (
            ApiV1OrganizationsIconUploadCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_id_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_provider_reference_error_component import (
            ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_scope_error_component import (
            ApiV1OrganizationsIconUploadCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_target_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_sla_window_days_error_component import (
            ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_target_error_component import (
            ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slo_window_days_error_component import (
            ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_slug_error_component import (
            ApiV1OrganizationsIconUploadCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_target_availability_error_component import (
            ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_upstream_system_id_error_component import (
            ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_urls_error_component import (
            ApiV1OrganizationsIconUploadCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_icon_upload_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsIconUploadCreateActiveErrorComponent
                | ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent
                | ApiV1OrganizationsIconUploadCreateAliasErrorComponent
                | ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent
                | ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent
                | ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent
                | ApiV1OrganizationsIconUploadCreateArchivedErrorComponent
                | ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsIconUploadCreateColorErrorComponent
                | ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent
                | ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent
                | ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent
                | ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent
                | ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent
                | ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent
                | ApiV1OrganizationsIconUploadCreateDomainsErrorComponent
                | ApiV1OrganizationsIconUploadCreateEmailsErrorComponent
                | ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent
                | ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent
                | ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsIconUploadCreateKindErrorComponent
                | ApiV1OrganizationsIconUploadCreateLabelsErrorComponent
                | ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent
                | ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent
                | ApiV1OrganizationsIconUploadCreateNameErrorComponent
                | ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent
                | ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent
                | ApiV1OrganizationsIconUploadCreatePriorityErrorComponent
                | ApiV1OrganizationsIconUploadCreateProviderErrorComponent
                | ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent
                | ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsIconUploadCreateScopeErrorComponent
                | ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent
                | ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent
                | ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent
                | ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent
                | ApiV1OrganizationsIconUploadCreateSlugErrorComponent
                | ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsIconUploadCreateUrlsErrorComponent
                | ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_0 = (
                        ApiV1OrganizationsIconUploadCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_1 = (
                        ApiV1OrganizationsIconUploadCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_2 = (
                        ApiV1OrganizationsIconUploadCreateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_3 = (
                        ApiV1OrganizationsIconUploadCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_4 = (
                        ApiV1OrganizationsIconUploadCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_5 = (
                        ApiV1OrganizationsIconUploadCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_6 = (
                        ApiV1OrganizationsIconUploadCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_7 = (
                        ApiV1OrganizationsIconUploadCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_8 = (
                        ApiV1OrganizationsIconUploadCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_9 = (
                        ApiV1OrganizationsIconUploadCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_10 = (
                        ApiV1OrganizationsIconUploadCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_11 = (
                        ApiV1OrganizationsIconUploadCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_12 = (
                        ApiV1OrganizationsIconUploadCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_13 = (
                        ApiV1OrganizationsIconUploadCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_14 = (
                        ApiV1OrganizationsIconUploadCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_15 = (
                        ApiV1OrganizationsIconUploadCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_16 = (
                        ApiV1OrganizationsIconUploadCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_17 = (
                        ApiV1OrganizationsIconUploadCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_18 = (
                        ApiV1OrganizationsIconUploadCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_19 = (
                        ApiV1OrganizationsIconUploadCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_20 = (
                        ApiV1OrganizationsIconUploadCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_21 = (
                        ApiV1OrganizationsIconUploadCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_22 = (
                        ApiV1OrganizationsIconUploadCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_23 = (
                        ApiV1OrganizationsIconUploadCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_24 = (
                        ApiV1OrganizationsIconUploadCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_25 = (
                        ApiV1OrganizationsIconUploadCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_26 = (
                        ApiV1OrganizationsIconUploadCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_27 = (
                        ApiV1OrganizationsIconUploadCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_28 = (
                        ApiV1OrganizationsIconUploadCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_29 = (
                        ApiV1OrganizationsIconUploadCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_30 = (
                        ApiV1OrganizationsIconUploadCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_31 = (
                        ApiV1OrganizationsIconUploadCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_32 = (
                        ApiV1OrganizationsIconUploadCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_33 = (
                        ApiV1OrganizationsIconUploadCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_34 = (
                        ApiV1OrganizationsIconUploadCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_35 = (
                        ApiV1OrganizationsIconUploadCreateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_36 = (
                        ApiV1OrganizationsIconUploadCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_37 = (
                        ApiV1OrganizationsIconUploadCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_38 = (
                        ApiV1OrganizationsIconUploadCreateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_39 = (
                        ApiV1OrganizationsIconUploadCreateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_40 = (
                        ApiV1OrganizationsIconUploadCreateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_41 = (
                        ApiV1OrganizationsIconUploadCreateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_42 = (
                        ApiV1OrganizationsIconUploadCreateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_43 = (
                        ApiV1OrganizationsIconUploadCreateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_44 = (
                        ApiV1OrganizationsIconUploadCreateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_45 = (
                        ApiV1OrganizationsIconUploadCreateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_46 = (
                        ApiV1OrganizationsIconUploadCreateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_47 = (
                        ApiV1OrganizationsIconUploadCreateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_48 = (
                        ApiV1OrganizationsIconUploadCreateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_49 = (
                        ApiV1OrganizationsIconUploadCreateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_50 = (
                        ApiV1OrganizationsIconUploadCreateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_51 = (
                        ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_52 = (
                        ApiV1OrganizationsIconUploadCreateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_53 = (
                        ApiV1OrganizationsIconUploadCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_54 = (
                        ApiV1OrganizationsIconUploadCreateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_55 = (
                        ApiV1OrganizationsIconUploadCreateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_56 = (
                        ApiV1OrganizationsIconUploadCreateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_57 = (
                        ApiV1OrganizationsIconUploadCreateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_58 = (
                        ApiV1OrganizationsIconUploadCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_59 = (
                        ApiV1OrganizationsIconUploadCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_60 = (
                        ApiV1OrganizationsIconUploadCreateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_61 = (
                        ApiV1OrganizationsIconUploadCreateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_62 = (
                        ApiV1OrganizationsIconUploadCreateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_63 = (
                        ApiV1OrganizationsIconUploadCreateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_64 = (
                        ApiV1OrganizationsIconUploadCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_65 = (
                        ApiV1OrganizationsIconUploadCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_66 = (
                        ApiV1OrganizationsIconUploadCreateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_67 = (
                        ApiV1OrganizationsIconUploadCreateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_68 = (
                        ApiV1OrganizationsIconUploadCreateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_69 = (
                        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_70 = (
                        ApiV1OrganizationsIconUploadCreateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_71 = (
                        ApiV1OrganizationsIconUploadCreateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_72 = (
                        ApiV1OrganizationsIconUploadCreateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_73 = (
                        ApiV1OrganizationsIconUploadCreateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_74 = (
                        ApiV1OrganizationsIconUploadCreateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_75 = (
                        ApiV1OrganizationsIconUploadCreateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_76 = (
                        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_77 = (
                        ApiV1OrganizationsIconUploadCreateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_78 = (
                        ApiV1OrganizationsIconUploadCreateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_79 = (
                        ApiV1OrganizationsIconUploadCreateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_80 = (
                        ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_81 = (
                        ApiV1OrganizationsIconUploadCreateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_82 = (
                        ApiV1OrganizationsIconUploadCreateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_83 = (
                        ApiV1OrganizationsIconUploadCreateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_84 = (
                        ApiV1OrganizationsIconUploadCreateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_85 = (
                        ApiV1OrganizationsIconUploadCreateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_86 = (
                        ApiV1OrganizationsIconUploadCreateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_87 = (
                        ApiV1OrganizationsIconUploadCreateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_88 = (
                        ApiV1OrganizationsIconUploadCreateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_89 = (
                        ApiV1OrganizationsIconUploadCreateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_90 = (
                        ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_91 = (
                        ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_92 = (
                        ApiV1OrganizationsIconUploadCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_93 = (
                        ApiV1OrganizationsIconUploadCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_94 = (
                        ApiV1OrganizationsIconUploadCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_95 = (
                        ApiV1OrganizationsIconUploadCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_icon_upload_create_error_type_96 = (
                        ApiV1OrganizationsIconUploadCreateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_icon_upload_create_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_icon_upload_create_error_type_97 = (
                    ApiV1OrganizationsIconUploadCreateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_icon_upload_create_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_icon_upload_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_icon_upload_create_validation_error.additional_properties = d
        return api_v1_organizations_icon_upload_create_validation_error

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
