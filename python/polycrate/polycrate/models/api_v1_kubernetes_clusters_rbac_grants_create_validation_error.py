from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_active_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_actual_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_addons_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_alias_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_annotations_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_api_server_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_at_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_reason_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_backup_schedules_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_baserow_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_credential_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_criticality_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_debug_mode_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_description_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_enabled_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_ignored_namespaces_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_display_name_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_gitlab_project_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_installed_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_host_cluster_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_infrastructure_cluster_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kind_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_ca_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_client_cert_expiry_date_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubernetes_version_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_labels_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_last_backup_import_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_managed_by_content_type_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_managed_by_object_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_name_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_non_field_errors_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_ignore_namespaces_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_loglevel_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_dns_record_created_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_service_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_id_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_reference_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_scope_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_target_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_target_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slug_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent,
    )
    from ..models.api_v1_kubernetes_clusters_rbac_grants_create_target_availability_error_component import (
        ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesClustersRbacGrantsCreateValidationError")


@_attrs_define
class ApiV1KubernetesClustersRbacGrantsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent |
            ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent
        | ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_active_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_actual_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_addons_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_alias_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_annotations_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_at_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_reason_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_baserow_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_credential_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_criticality_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_debug_mode_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_description_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_display_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_installed_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kind_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_labels_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_service_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_reference_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_scope_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slug_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_target_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent
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
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_active_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_actual_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_addons_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_alias_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_annotations_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_api_server_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_at_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_archived_reason_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_backup_schedules_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_baserow_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_credential_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_criticality_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_debug_mode_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_description_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_discovery_ignored_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_display_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_gitlab_project_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_installed_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_host_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_is_infrastructure_cluster_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kind_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_ca_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubeconfig_client_cert_expiry_date_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_kubernetes_version_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_labels_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_last_backup_import_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_managed_by_content_type_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_managed_by_object_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_name_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_non_field_errors_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_ignore_namespaces_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_operator_loglevel_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_dns_record_created_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_platform_service_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_id_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_provider_reference_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_scope_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_sla_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slo_target_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_slug_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_clusters_rbac_grants_create_target_availability_error_component import (
            ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent
                | ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_0 = (
                        ApiV1KubernetesClustersRbacGrantsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_1 = (
                        ApiV1KubernetesClustersRbacGrantsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_2 = (
                        ApiV1KubernetesClustersRbacGrantsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_3 = (
                        ApiV1KubernetesClustersRbacGrantsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_4 = (
                        ApiV1KubernetesClustersRbacGrantsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_5 = (
                        ApiV1KubernetesClustersRbacGrantsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_6 = (
                        ApiV1KubernetesClustersRbacGrantsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_7 = (
                        ApiV1KubernetesClustersRbacGrantsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_8 = (
                        ApiV1KubernetesClustersRbacGrantsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_9 = (
                        ApiV1KubernetesClustersRbacGrantsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_10 = (
                        ApiV1KubernetesClustersRbacGrantsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_11 = (
                        ApiV1KubernetesClustersRbacGrantsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_12 = (
                        ApiV1KubernetesClustersRbacGrantsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_13 = (
                        ApiV1KubernetesClustersRbacGrantsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_14 = (
                        ApiV1KubernetesClustersRbacGrantsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_15 = (
                        ApiV1KubernetesClustersRbacGrantsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_16 = (
                        ApiV1KubernetesClustersRbacGrantsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_17 = (
                        ApiV1KubernetesClustersRbacGrantsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_18 = (
                        ApiV1KubernetesClustersRbacGrantsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_19 = (
                        ApiV1KubernetesClustersRbacGrantsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_20 = (
                        ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_21 = (
                        ApiV1KubernetesClustersRbacGrantsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_22 = (
                        ApiV1KubernetesClustersRbacGrantsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_23 = (
                        ApiV1KubernetesClustersRbacGrantsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_24 = (
                        ApiV1KubernetesClustersRbacGrantsCreateKubernetesVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_25 = (
                        ApiV1KubernetesClustersRbacGrantsCreateInstalledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_26 = (
                        ApiV1KubernetesClustersRbacGrantsCreateIsHostClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_27 = (
                        ApiV1KubernetesClustersRbacGrantsCreateIsInfrastructureClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_28 = (
                        ApiV1KubernetesClustersRbacGrantsCreateKubeconfigCaCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_29 = (
                        ApiV1KubernetesClustersRbacGrantsCreateKubeconfigClientCertExpiryDateErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_30 = (
                        ApiV1KubernetesClustersRbacGrantsCreateApiServerCertExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_31 = (
                        ApiV1KubernetesClustersRbacGrantsCreateCredentialErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_32 = (
                        ApiV1KubernetesClustersRbacGrantsCreateDiscoveryIgnoredNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_33 = (
                        ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_34 = (
                        ApiV1KubernetesClustersRbacGrantsCreateOperatorIgnoreNamespacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_35 = (
                        ApiV1KubernetesClustersRbacGrantsCreateAliasErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_36 = (
                        ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_37 = (
                        ApiV1KubernetesClustersRbacGrantsCreateAddonsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_38 = (
                        ApiV1KubernetesClustersRbacGrantsCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_39 = (
                        ApiV1KubernetesClustersRbacGrantsCreateBackupSchedulesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_40 = (
                        ApiV1KubernetesClustersRbacGrantsCreateBaserowIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_41 = (
                        ApiV1KubernetesClustersRbacGrantsCreateGitlabProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_42 = (
                        ApiV1KubernetesClustersRbacGrantsCreateLastBackupImportErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_43 = (
                        ApiV1KubernetesClustersRbacGrantsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_44 = (
                        ApiV1KubernetesClustersRbacGrantsCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_45 = (
                        ApiV1KubernetesClustersRbacGrantsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_46 = (
                    ApiV1KubernetesClustersRbacGrantsCreateManagedByObjectIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_clusters_rbac_grants_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_clusters_rbac_grants_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_clusters_rbac_grants_create_validation_error.additional_properties = d
        return api_v1_kubernetes_clusters_rbac_grants_create_validation_error

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
