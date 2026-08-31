from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_active_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_actual_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_addons_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_alias_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_annotations_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_at_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_reason_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_backup_schedules_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_baserow_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_credential_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_criticality_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_debug_mode_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_description_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_display_name_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_installed_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_host_cluster_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kind_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubernetes_version_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_labels_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_last_backup_import_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_name_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_loglevel_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_service_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_reference_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_scope_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_target_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_target_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slug_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_target_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersRbacGrantsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesClustersRbacGrantsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent |
            ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent
        | ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_active_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_addons_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_alias_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_annotations_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_at_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_baserow_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_credential_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_criticality_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_description_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_display_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_installed_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kind_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_labels_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_service_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_scope_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slug_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_target_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data,
                ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent
            ):
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
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_active_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_actual_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_addons_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_alias_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_annotations_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_at_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_archived_reason_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_backup_schedules_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_baserow_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_credential_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_criticality_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_debug_mode_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_description_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_display_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_installed_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_host_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kind_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_kubernetes_version_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_labels_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_last_backup_import_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_operator_loglevel_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_platform_service_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_provider_reference_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_scope_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_sla_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slo_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_slug_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent,
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_partial_update_target_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent
                | ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_0 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_1 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_2 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_3 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_4 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_5 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_6 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_7 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_8 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_9 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_10 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_11 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_12 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_13 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_14 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_15 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_16 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_17 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_18 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_19 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_20 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_21 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_22 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_23 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_24 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_25 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_26 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_27 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateIsInfrastructureClusterErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_28 = ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigCaCertExpiryDateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_29 = ApiV1KubernetesClustersRbacGrantsPartialUpdateKubeconfigClientCertExpiryDateErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_30 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateApiServerCertExpiryDateErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_31 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_32 = ApiV1KubernetesClustersRbacGrantsPartialUpdateDiscoveryIgnoredNamespacesErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_33 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_34 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateOperatorIgnoreNamespacesErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_35 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_36 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_37 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_38 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_39 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_40 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_41 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_42 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_43 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_44 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_45 = (
                        ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_46 = (
                    ApiV1KubernetesClustersRbacGrantsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_partial_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_rbac_grants_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_rbac_grants_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_rbac_grants_partial_update_validation_error

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
