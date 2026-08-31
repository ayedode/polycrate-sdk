from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_organizations_archive_create_active_error_component import (
        ApiV1OrganizationsArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_actual_availability_error_component import (
        ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_alias_error_component import (
        ApiV1OrganizationsArchiveCreateAliasErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_annotations_error_component import (
        ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
        ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_archived_at_error_component import (
        ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_archived_by_error_component import (
        ApiV1OrganizationsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_archived_error_component import (
        ApiV1OrganizationsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_archived_reason_error_component import (
        ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_active_downtimes_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_active_maintenances_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_endpoint_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_endpoint_down_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_firing_alerts_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_k8s_cluster_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_lb_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_in_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_out_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_logs_30d_error_component import (
        ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_member_active_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_member_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_metrics_30d_avg_error_component import (
        ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_metrics_updated_at_error_component import (
        ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_open_incidents_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_product_cost_updated_at_error_component import (
        ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_s3_bucket_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_s3_object_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_s3_storage_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_total_product_cost_error_component import (
        ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_volume_capacity_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_volume_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_cached_workspace_count_error_component import (
        ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_color_error_component import (
        ApiV1OrganizationsArchiveCreateColorErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_created_by_component_error_component import (
        ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_created_by_user_error_component import (
        ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_criticality_error_component import (
        ApiV1OrganizationsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_debug_mode_error_component import (
        ApiV1OrganizationsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_description_error_component import (
        ApiV1OrganizationsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_discovery_enabled_error_component import (
        ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_display_name_error_component import (
        ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_domains_error_component import (
        ApiV1OrganizationsArchiveCreateDomainsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_emails_error_component import (
        ApiV1OrganizationsArchiveCreateEmailsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_endpoint_monitoring_mode_error_component import (
        ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_endpoint_monitors_error_component import (
        ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_gitlab_group_id_error_component import (
        ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_gitlab_group_url_error_component import (
        ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_grafana_org_id_error_component import (
        ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_group_id_error_component import (
        ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_project_id_error_component import (
        ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_project_membership_id_error_component import (
        ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_quota_hard_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_quota_updated_at_error_component import (
        ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_harbor_quota_used_bytes_error_component import (
        ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_icon_content_type_error_component import (
        ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_icon_filename_error_component import (
        ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_keycloak_role_group_ids_error_component import (
        ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_keycloak_tenant_enabled_error_component import (
        ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_keycloak_tenant_id_error_component import (
        ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_keycloak_tenant_name_error_component import (
        ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_kind_error_component import (
        ApiV1OrganizationsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_labels_error_component import (
        ApiV1OrganizationsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_legal_name_error_component import (
        ApiV1OrganizationsArchiveCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_loopback_org_id_error_component import (
        ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_loopback_project_id_error_component import (
        ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_managed_by_content_type_error_component import (
        ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_managed_by_object_id_error_component import (
        ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_modified_by_user_error_component import (
        ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_name_error_component import (
        ApiV1OrganizationsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_non_field_errors_error_component import (
        ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_observability_metrics_error_component import (
        ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_owner_id_error_component import (
        ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_platform_dns_record_created_error_component import (
        ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_platform_service_error_component import (
        ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_priority_error_component import (
        ApiV1OrganizationsArchiveCreatePriorityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_provider_error_component import (
        ApiV1OrganizationsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_provider_id_error_component import (
        ApiV1OrganizationsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_provider_reference_error_component import (
        ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_reconciliation_enabled_error_component import (
        ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_rocketchat_channel_announcement_error_component import (
        ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_rocketchat_channel_avatar_hash_error_component import (
        ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_rocketchat_channel_id_error_component import (
        ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_rocketchat_channel_name_error_component import (
        ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_scope_error_component import (
        ApiV1OrganizationsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_sla_availability_error_component import (
        ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_sla_target_error_component import (
        ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_sla_window_days_error_component import (
        ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_slo_availability_error_component import (
        ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_slo_target_error_component import (
        ApiV1OrganizationsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_slo_window_days_error_component import (
        ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_slug_error_component import (
        ApiV1OrganizationsArchiveCreateSlugErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_target_availability_error_component import (
        ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_unified_harbor_credential_error_component import (
        ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_upstream_organization_id_error_component import (
        ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_upstream_system_id_error_component import (
        ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_urls_error_component import (
        ApiV1OrganizationsArchiveCreateUrlsErrorComponent,
    )
    from ..models.api_v1_organizations_archive_create_workspace_default_owner_id_error_component import (
        ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1OrganizationsArchiveCreateValidationError")


@_attrs_define
class ApiV1OrganizationsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1OrganizationsArchiveCreateActiveErrorComponent |
            ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1OrganizationsArchiveCreateAliasErrorComponent | ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent |
            ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent |
            ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent |
            ApiV1OrganizationsArchiveCreateArchivedByErrorComponent | ApiV1OrganizationsArchiveCreateArchivedErrorComponent
            | ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent |
            ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent |
            ApiV1OrganizationsArchiveCreateColorErrorComponent |
            ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent |
            ApiV1OrganizationsArchiveCreateCriticalityErrorComponent |
            ApiV1OrganizationsArchiveCreateDebugModeErrorComponent |
            ApiV1OrganizationsArchiveCreateDescriptionErrorComponent |
            ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent | ApiV1OrganizationsArchiveCreateDomainsErrorComponent
            | ApiV1OrganizationsArchiveCreateEmailsErrorComponent |
            ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent |
            ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent |
            ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent |
            ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent |
            ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent |
            ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent |
            ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent |
            ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent |
            ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent |
            ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent |
            ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent |
            ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent |
            ApiV1OrganizationsArchiveCreateKindErrorComponent | ApiV1OrganizationsArchiveCreateLabelsErrorComponent |
            ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1OrganizationsArchiveCreateLegalNameErrorComponent |
            ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent |
            ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent |
            ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent | ApiV1OrganizationsArchiveCreateNameErrorComponent
            | ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent |
            ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent |
            ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent |
            ApiV1OrganizationsArchiveCreatePriorityErrorComponent | ApiV1OrganizationsArchiveCreateProviderErrorComponent |
            ApiV1OrganizationsArchiveCreateProviderIdErrorComponent |
            ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent |
            ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent |
            ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent |
            ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent |
            ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent |
            ApiV1OrganizationsArchiveCreateScopeErrorComponent |
            ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent |
            ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1OrganizationsArchiveCreateSloTargetErrorComponent |
            ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent | ApiV1OrganizationsArchiveCreateSlugErrorComponent |
            ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent |
            ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent |
            ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent |
            ApiV1OrganizationsArchiveCreateUrlsErrorComponent |
            ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1OrganizationsArchiveCreateActiveErrorComponent
        | ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1OrganizationsArchiveCreateAliasErrorComponent
        | ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent
        | ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent
        | ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent
        | ApiV1OrganizationsArchiveCreateArchivedByErrorComponent
        | ApiV1OrganizationsArchiveCreateArchivedErrorComponent
        | ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent
        | ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent
        | ApiV1OrganizationsArchiveCreateColorErrorComponent
        | ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent
        | ApiV1OrganizationsArchiveCreateCriticalityErrorComponent
        | ApiV1OrganizationsArchiveCreateDebugModeErrorComponent
        | ApiV1OrganizationsArchiveCreateDescriptionErrorComponent
        | ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent
        | ApiV1OrganizationsArchiveCreateDomainsErrorComponent
        | ApiV1OrganizationsArchiveCreateEmailsErrorComponent
        | ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent
        | ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent
        | ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent
        | ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent
        | ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent
        | ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent
        | ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent
        | ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent
        | ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent
        | ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent
        | ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent
        | ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent
        | ApiV1OrganizationsArchiveCreateKindErrorComponent
        | ApiV1OrganizationsArchiveCreateLabelsErrorComponent
        | ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1OrganizationsArchiveCreateLegalNameErrorComponent
        | ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent
        | ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent
        | ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent
        | ApiV1OrganizationsArchiveCreateNameErrorComponent
        | ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent
        | ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent
        | ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent
        | ApiV1OrganizationsArchiveCreatePriorityErrorComponent
        | ApiV1OrganizationsArchiveCreateProviderErrorComponent
        | ApiV1OrganizationsArchiveCreateProviderIdErrorComponent
        | ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent
        | ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent
        | ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent
        | ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent
        | ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent
        | ApiV1OrganizationsArchiveCreateScopeErrorComponent
        | ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent
        | ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1OrganizationsArchiveCreateSloTargetErrorComponent
        | ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1OrganizationsArchiveCreateSlugErrorComponent
        | ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent
        | ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent
        | ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent
        | ApiV1OrganizationsArchiveCreateUrlsErrorComponent
        | ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_organizations_archive_create_active_error_component import (
            ApiV1OrganizationsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_actual_availability_error_component import (
            ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_alias_error_component import (
            ApiV1OrganizationsArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_annotations_error_component import (
            ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_at_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_by_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_reason_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_member_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_volume_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_color_error_component import (
            ApiV1OrganizationsArchiveCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_created_by_component_error_component import (
            ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_created_by_user_error_component import (
            ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_criticality_error_component import (
            ApiV1OrganizationsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_debug_mode_error_component import (
            ApiV1OrganizationsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_description_error_component import (
            ApiV1OrganizationsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_discovery_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_display_name_error_component import (
            ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_domains_error_component import (
            ApiV1OrganizationsArchiveCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_emails_error_component import (
            ApiV1OrganizationsArchiveCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_grafana_org_id_error_component import (
            ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_group_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_project_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_icon_content_type_error_component import (
            ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_icon_filename_error_component import (
            ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_kind_error_component import (
            ApiV1OrganizationsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_labels_error_component import (
            ApiV1OrganizationsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_legal_name_error_component import (
            ApiV1OrganizationsArchiveCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_loopback_org_id_error_component import (
            ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_loopback_project_id_error_component import (
            ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_modified_by_user_error_component import (
            ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_name_error_component import (
            ApiV1OrganizationsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_non_field_errors_error_component import (
            ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_observability_metrics_error_component import (
            ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_owner_id_error_component import (
            ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_platform_service_error_component import (
            ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_priority_error_component import (
            ApiV1OrganizationsArchiveCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_error_component import (
            ApiV1OrganizationsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_id_error_component import (
            ApiV1OrganizationsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_reference_error_component import (
            ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_scope_error_component import (
            ApiV1OrganizationsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_availability_error_component import (
            ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_target_error_component import (
            ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_window_days_error_component import (
            ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_availability_error_component import (
            ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_target_error_component import (
            ApiV1OrganizationsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_window_days_error_component import (
            ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slug_error_component import (
            ApiV1OrganizationsArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_target_availability_error_component import (
            ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_upstream_system_id_error_component import (
            ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_urls_error_component import (
            ApiV1OrganizationsArchiveCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateDomainsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateColorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreatePriorityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateUrlsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent):
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
        from ..models.api_v1_organizations_archive_create_active_error_component import (
            ApiV1OrganizationsArchiveCreateActiveErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_actual_availability_error_component import (
            ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_alias_error_component import (
            ApiV1OrganizationsArchiveCreateAliasErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_annotations_error_component import (
            ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_apm_vmuser_manifest_last_applied_sha_256_error_component import (
            ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_at_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_by_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_archived_reason_error_component import (
            ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_active_downtimes_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_active_maintenances_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_endpoint_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_endpoint_down_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_firing_alerts_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_k8s_cluster_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_in_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_lb_traffic_30d_out_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_logs_30d_error_component import (
            ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_member_active_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_member_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_metrics_30d_avg_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_metrics_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_open_incidents_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_product_cost_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_bucket_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_object_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_s3_storage_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_total_product_cost_error_component import (
            ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_volume_capacity_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_volume_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_cached_workspace_count_error_component import (
            ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_color_error_component import (
            ApiV1OrganizationsArchiveCreateColorErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_created_by_component_error_component import (
            ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_created_by_user_error_component import (
            ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_criticality_error_component import (
            ApiV1OrganizationsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_debug_mode_error_component import (
            ApiV1OrganizationsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_description_error_component import (
            ApiV1OrganizationsArchiveCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_discovery_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_display_name_error_component import (
            ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_domains_error_component import (
            ApiV1OrganizationsArchiveCreateDomainsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_emails_error_component import (
            ApiV1OrganizationsArchiveCreateEmailsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_endpoint_monitoring_mode_error_component import (
            ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_endpoint_monitors_error_component import (
            ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_gitlab_group_id_error_component import (
            ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_gitlab_group_url_error_component import (
            ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_grafana_org_id_error_component import (
            ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_group_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_project_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_project_membership_id_error_component import (
            ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_hard_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_updated_at_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_harbor_quota_used_bytes_error_component import (
            ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_icon_content_type_error_component import (
            ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_icon_filename_error_component import (
            ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_role_group_ids_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_id_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_keycloak_tenant_name_error_component import (
            ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_kind_error_component import (
            ApiV1OrganizationsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_labels_error_component import (
            ApiV1OrganizationsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_legal_name_error_component import (
            ApiV1OrganizationsArchiveCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_loopback_org_id_error_component import (
            ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_loopback_project_id_error_component import (
            ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_managed_by_content_type_error_component import (
            ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_managed_by_object_id_error_component import (
            ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_modified_by_user_error_component import (
            ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_name_error_component import (
            ApiV1OrganizationsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_non_field_errors_error_component import (
            ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_observability_metrics_error_component import (
            ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_owner_id_error_component import (
            ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_platform_dns_record_created_error_component import (
            ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_platform_service_error_component import (
            ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_priority_error_component import (
            ApiV1OrganizationsArchiveCreatePriorityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_error_component import (
            ApiV1OrganizationsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_id_error_component import (
            ApiV1OrganizationsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_provider_reference_error_component import (
            ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_reconciliation_enabled_error_component import (
            ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_announcement_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_avatar_hash_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_id_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_rocketchat_channel_name_error_component import (
            ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_scope_error_component import (
            ApiV1OrganizationsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_availability_error_component import (
            ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_target_error_component import (
            ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_sla_window_days_error_component import (
            ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_availability_error_component import (
            ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_target_error_component import (
            ApiV1OrganizationsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slo_window_days_error_component import (
            ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_slug_error_component import (
            ApiV1OrganizationsArchiveCreateSlugErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_target_availability_error_component import (
            ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_unified_harbor_credential_error_component import (
            ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_upstream_organization_id_error_component import (
            ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_upstream_system_id_error_component import (
            ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_urls_error_component import (
            ApiV1OrganizationsArchiveCreateUrlsErrorComponent,
        )
        from ..models.api_v1_organizations_archive_create_workspace_default_owner_id_error_component import (
            ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1OrganizationsArchiveCreateActiveErrorComponent
                | ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1OrganizationsArchiveCreateAliasErrorComponent
                | ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent
                | ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent
                | ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent
                | ApiV1OrganizationsArchiveCreateArchivedByErrorComponent
                | ApiV1OrganizationsArchiveCreateArchivedErrorComponent
                | ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent
                | ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent
                | ApiV1OrganizationsArchiveCreateColorErrorComponent
                | ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent
                | ApiV1OrganizationsArchiveCreateCriticalityErrorComponent
                | ApiV1OrganizationsArchiveCreateDebugModeErrorComponent
                | ApiV1OrganizationsArchiveCreateDescriptionErrorComponent
                | ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent
                | ApiV1OrganizationsArchiveCreateDomainsErrorComponent
                | ApiV1OrganizationsArchiveCreateEmailsErrorComponent
                | ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent
                | ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent
                | ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent
                | ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent
                | ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent
                | ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent
                | ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent
                | ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent
                | ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent
                | ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent
                | ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent
                | ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent
                | ApiV1OrganizationsArchiveCreateKindErrorComponent
                | ApiV1OrganizationsArchiveCreateLabelsErrorComponent
                | ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1OrganizationsArchiveCreateLegalNameErrorComponent
                | ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent
                | ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent
                | ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent
                | ApiV1OrganizationsArchiveCreateNameErrorComponent
                | ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent
                | ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent
                | ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent
                | ApiV1OrganizationsArchiveCreatePriorityErrorComponent
                | ApiV1OrganizationsArchiveCreateProviderErrorComponent
                | ApiV1OrganizationsArchiveCreateProviderIdErrorComponent
                | ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent
                | ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent
                | ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent
                | ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent
                | ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent
                | ApiV1OrganizationsArchiveCreateScopeErrorComponent
                | ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent
                | ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1OrganizationsArchiveCreateSloTargetErrorComponent
                | ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1OrganizationsArchiveCreateSlugErrorComponent
                | ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent
                | ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent
                | ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent
                | ApiV1OrganizationsArchiveCreateUrlsErrorComponent
                | ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_0 = (
                        ApiV1OrganizationsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_1 = (
                        ApiV1OrganizationsArchiveCreateOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_2 = (
                        ApiV1OrganizationsArchiveCreateWorkspaceDefaultOwnerIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_3 = (
                        ApiV1OrganizationsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_4 = (
                        ApiV1OrganizationsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_5 = (
                        ApiV1OrganizationsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_6 = (
                        ApiV1OrganizationsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_7 = (
                        ApiV1OrganizationsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_8 = (
                        ApiV1OrganizationsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_9 = (
                        ApiV1OrganizationsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_10 = (
                        ApiV1OrganizationsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_11 = (
                        ApiV1OrganizationsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_12 = (
                        ApiV1OrganizationsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_13 = (
                        ApiV1OrganizationsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_14 = (
                        ApiV1OrganizationsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_15 = (
                        ApiV1OrganizationsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_16 = (
                        ApiV1OrganizationsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_17 = (
                        ApiV1OrganizationsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_18 = (
                        ApiV1OrganizationsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_19 = (
                        ApiV1OrganizationsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_20 = (
                        ApiV1OrganizationsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_21 = (
                        ApiV1OrganizationsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_22 = (
                        ApiV1OrganizationsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_23 = (
                        ApiV1OrganizationsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_24 = (
                        ApiV1OrganizationsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_25 = (
                        ApiV1OrganizationsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_26 = (
                        ApiV1OrganizationsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_27 = (
                        ApiV1OrganizationsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_28 = (
                        ApiV1OrganizationsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_29 = (
                        ApiV1OrganizationsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_30 = (
                        ApiV1OrganizationsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_31 = (
                        ApiV1OrganizationsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_32 = (
                        ApiV1OrganizationsArchiveCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_33 = (
                        ApiV1OrganizationsArchiveCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_34 = (
                        ApiV1OrganizationsArchiveCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_35 = (
                        ApiV1OrganizationsArchiveCreateDomainsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_36 = (
                        ApiV1OrganizationsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_37 = (
                        ApiV1OrganizationsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_38 = (
                        ApiV1OrganizationsArchiveCreateKeycloakTenantEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_39 = (
                        ApiV1OrganizationsArchiveCreateKeycloakTenantNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_40 = (
                        ApiV1OrganizationsArchiveCreateKeycloakTenantIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_41 = (
                        ApiV1OrganizationsArchiveCreateKeycloakRoleGroupIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_42 = (
                        ApiV1OrganizationsArchiveCreateHarborGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_43 = (
                        ApiV1OrganizationsArchiveCreateHarborProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_44 = (
                        ApiV1OrganizationsArchiveCreateHarborProjectMembershipIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_45 = (
                        ApiV1OrganizationsArchiveCreateHarborQuotaUsedBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_46 = (
                        ApiV1OrganizationsArchiveCreateHarborQuotaHardBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_47 = (
                        ApiV1OrganizationsArchiveCreateHarborQuotaUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_48 = (
                        ApiV1OrganizationsArchiveCreateGrafanaOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_49 = (
                        ApiV1OrganizationsArchiveCreateGitlabGroupIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_50 = (
                        ApiV1OrganizationsArchiveCreateGitlabGroupUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_51 = (
                        ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_52 = (
                        ApiV1OrganizationsArchiveCreateColorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_53 = (
                        ApiV1OrganizationsArchiveCreatePriorityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_54 = (
                        ApiV1OrganizationsArchiveCreateUpstreamOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_55 = (
                        ApiV1OrganizationsArchiveCreateUpstreamSystemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_56 = (
                        ApiV1OrganizationsArchiveCreateLoopbackOrgIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_57 = (
                        ApiV1OrganizationsArchiveCreateLoopbackProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_58 = (
                        ApiV1OrganizationsArchiveCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_59 = (
                        ApiV1OrganizationsArchiveCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_59
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_60 = (
                        ApiV1OrganizationsArchiveCreateRocketchatChannelIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_60
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_61 = (
                        ApiV1OrganizationsArchiveCreateRocketchatChannelNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_61
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_62 = (
                        ApiV1OrganizationsArchiveCreateRocketchatChannelAvatarHashErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_62
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_63 = (
                        ApiV1OrganizationsArchiveCreateRocketchatChannelAnnouncementErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_63
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_64 = (
                        ApiV1OrganizationsArchiveCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_64
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_65 = (
                        ApiV1OrganizationsArchiveCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_65
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_66 = (
                        ApiV1OrganizationsArchiveCreateApmVmuserManifestLastAppliedSha256ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_66
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_67 = (
                        ApiV1OrganizationsArchiveCreateObservabilityMetricsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_67
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_68 = (
                        ApiV1OrganizationsArchiveCreateCachedS3StorageBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_68
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_69 = (
                        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_69
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_70 = (
                        ApiV1OrganizationsArchiveCreateCachedLogs30DErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_70
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_71 = (
                        ApiV1OrganizationsArchiveCreateCachedMetrics30DAvgErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_71
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_72 = (
                        ApiV1OrganizationsArchiveCreateCachedMetricsUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_72
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_73 = (
                        ApiV1OrganizationsArchiveCreateCachedS3BucketCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_73
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_74 = (
                        ApiV1OrganizationsArchiveCreateCachedS3ObjectCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_74
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_75 = (
                        ApiV1OrganizationsArchiveCreateCachedLbCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_75
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_76 = (
                        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DInBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_76
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_77 = (
                        ApiV1OrganizationsArchiveCreateCachedLbTraffic30DOutBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_77
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_78 = (
                        ApiV1OrganizationsArchiveCreateCachedVolumeCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_78
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_79 = (
                        ApiV1OrganizationsArchiveCreateCachedVolumeCapacityBytesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_79
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_80 = (
                        ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_80
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_81 = (
                        ApiV1OrganizationsArchiveCreateCachedWorkspaceCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_81
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_82 = (
                        ApiV1OrganizationsArchiveCreateCachedEndpointCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_82
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_83 = (
                        ApiV1OrganizationsArchiveCreateCachedEndpointDownCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_83
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_84 = (
                        ApiV1OrganizationsArchiveCreateCachedMemberCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_84
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_85 = (
                        ApiV1OrganizationsArchiveCreateCachedMemberActiveCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_85
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_86 = (
                        ApiV1OrganizationsArchiveCreateCachedActiveMaintenancesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_86
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_87 = (
                        ApiV1OrganizationsArchiveCreateCachedOpenIncidentsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_87
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_88 = (
                        ApiV1OrganizationsArchiveCreateCachedActiveDowntimesCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_88
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_89 = (
                        ApiV1OrganizationsArchiveCreateCachedFiringAlertsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_89
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_90 = (
                        ApiV1OrganizationsArchiveCreateCachedTotalProductCostErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_90
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_91 = (
                        ApiV1OrganizationsArchiveCreateCachedProductCostUpdatedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_91
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_92 = (
                        ApiV1OrganizationsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_92
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_93 = (
                        ApiV1OrganizationsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_93
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_94 = (
                        ApiV1OrganizationsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_94
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_95 = (
                        ApiV1OrganizationsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_95
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_organizations_archive_create_error_type_96 = (
                        ApiV1OrganizationsArchiveCreateUnifiedHarborCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_organizations_archive_create_error_type_96
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_organizations_archive_create_error_type_97 = (
                    ApiV1OrganizationsArchiveCreateEndpointMonitorsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_organizations_archive_create_error_type_97

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_organizations_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_organizations_archive_create_validation_error.additional_properties = d
        return api_v1_organizations_archive_create_validation_error

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
